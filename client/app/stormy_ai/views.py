"""Render the latest Stormy AI Markdown document stored in S3."""

from urllib.parse import urlparse

import boto3
import bleach
import markdown
from botocore.exceptions import BotoCoreError, ClientError
from flask import Blueprint, current_app, render_template
from markupsafe import Markup


stormy_ai_bp = Blueprint("stormy_ai", __name__, url_prefix="/stormy-ai")
LATEST_POINTER_URI = "s3://stormy-ai-files/latest.txt"
ALLOWED_MARKDOWN_TAGS = {
    "a",
    "blockquote",
    "br",
    "code",
    "del",
    "em",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "hr",
    "img",
    "li",
    "ol",
    "p",
    "pre",
    "strong",
    "table",
    "tbody",
    "td",
    "th",
    "thead",
    "tr",
    "ul",
}
ALLOWED_MARKDOWN_ATTRIBUTES = {
    "a": ["href", "title"],
    "code": ["class"],
    "img": ["src", "alt", "title", "width", "height"],
    "th": ["align"],
    "td": ["align"],
}
ALLOWED_MARKDOWN_PROTOCOLS = {"http", "https", "mailto"}


def parse_s3_uri(uri):
    """Return the bucket and key from a fully qualified S3 URI."""
    parsed = urlparse(uri.strip())
    key = parsed.path.lstrip("/")
    if (
        parsed.scheme != "s3"
        or not parsed.netloc
        or not key
        or parsed.params
        or parsed.query
        or parsed.fragment
    ):
        raise ValueError(f"Invalid S3 URI: {uri!r}")
    return parsed.netloc, key


def read_s3_text(s3_client, uri):
    """Read a UTF-8 text object from S3."""
    bucket, key = parse_s3_uri(uri)
    response = s3_client.get_object(Bucket=bucket, Key=key)
    return response["Body"].read().decode("utf-8")


def get_latest_markdown(s3_client=None):
    """Follow the latest-document pointer and return its Markdown content."""
    s3_client = s3_client or boto3.client("s3")
    markdown_uri = read_s3_text(s3_client, LATEST_POINTER_URI).strip()
    if not markdown_uri:
        raise ValueError("The latest Markdown pointer is empty")
    return read_s3_text(s3_client, markdown_uri)


def render_markdown(markdown_text):
    """Render Markdown and allow only presentation-safe HTML."""
    rendered = markdown.markdown(
        markdown_text,
        extensions=["extra", "sane_lists"],
    )
    sanitized = bleach.clean(
        rendered,
        tags=ALLOWED_MARKDOWN_TAGS,
        attributes=ALLOWED_MARKDOWN_ATTRIBUTES,
        protocols=ALLOWED_MARKDOWN_PROTOCOLS,
        strip=True,
    )
    return Markup(sanitized)


@stormy_ai_bp.route("/")
def latest():
    """Render the Markdown document referenced by the S3 pointer."""
    try:
        markdown_text = get_latest_markdown()
        rendered_markdown = render_markdown(markdown_text)
        load_error = None
        status_code = 200
    except (BotoCoreError, ClientError, KeyError, UnicodeDecodeError, ValueError):
        current_app.logger.exception("Unable to load the latest Stormy AI document")
        rendered_markdown = None
        load_error = (
            "The latest Stormy AI report is temporarily unavailable. "
            "Please try again later."
        )
        status_code = 503

    return (
        render_template(
            "stormy_ai.html",
            title="\\\\Stormy AI\\\\",
            title_img="weather.png",
            rendered_markdown=rendered_markdown,
            load_error=load_error,
        ),
        status_code,
    )


@stormy_ai_bp.route("/about/")
def about():
    """Tell the engineering and meteorological story behind Stormy AI."""
    return render_template(
        "stormy_ai_about.html",
        title="\\\\Stormy AI Technical Deep Dive\\\\",
        title_img="weather.png",
    )
