"""Render the daily AI news briefing from a local Markdown file."""

from pathlib import Path

from flask import Blueprint, current_app, render_template

from app.stormy_ai.views import render_markdown


ai_news_bp = Blueprint("ai_news", __name__, url_prefix="/ai-news")
hermes_bp = Blueprint("hermes", __name__)
MARKDOWN_PATH = Path(__file__).resolve().parent / "ai_news.md"


def get_ai_news_markdown(path=None):
    """Return the daily AI news Markdown."""
    markdown_path = MARKDOWN_PATH if path is None else Path(path)
    text = markdown_path.read_text(encoding="utf-8")
    if not text.strip():
        raise ValueError("The AI news Markdown file is empty")
    return text


@ai_news_bp.route("/")
def index():
    """Render the Markdown briefing written by the daily update process."""
    try:
        rendered_markdown = render_markdown(get_ai_news_markdown())
        load_error = None
        status_code = 200
    except (OSError, UnicodeDecodeError, ValueError):
        current_app.logger.exception("Unable to load the AI news document")
        rendered_markdown = None
        load_error = (
            "Today's AI news is temporarily unavailable. "
            "Please try again later."
        )
        status_code = 503

    return (
        render_template(
            "ai_news.html",
            title="\\\\AI News\\\\",
            title_img="project.png",
            rendered_markdown=rendered_markdown,
            load_error=load_error,
        ),
        status_code,
    )


@hermes_bp.route("/hermes/")
def blog():
    """Portfolio post about the personal Hermes agent."""
    return render_template(
        "hermes.html",
        title="\\\\Hermes\\\\",
        title_img="project.png",
    )
