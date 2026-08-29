from io import BytesIO

import pytest

from app.stormy_ai.views import get_latest_markdown, parse_s3_uri, render_markdown


class FakeS3Client:
    def __init__(self, objects):
        self.objects = objects
        self.requests = []

    def get_object(self, Bucket, Key):
        self.requests.append((Bucket, Key))
        return {"Body": BytesIO(self.objects[(Bucket, Key)].encode("utf-8"))}


def test_parse_s3_uri():
    assert parse_s3_uri("s3://example-bucket/reports/latest.md") == (
        "example-bucket",
        "reports/latest.md",
    )


@pytest.mark.parametrize("uri", ["", "https://bucket/key", "s3://bucket", "s3:///key"])
def test_parse_s3_uri_rejects_invalid_uri(uri):
    with pytest.raises(ValueError):
        parse_s3_uri(uri)


def test_get_latest_markdown_follows_pointer():
    s3_client = FakeS3Client(
        {
            ("stormy-ai-files", "latest.txt"): "s3://reports/daily/latest.md\n",
            ("reports", "daily/latest.md"): "# Today's report",
        }
    )

    assert get_latest_markdown(s3_client) == "# Today's report"
    assert s3_client.requests == [
        ("stormy-ai-files", "latest.txt"),
        ("reports", "daily/latest.md"),
    ]


def test_stormy_ai_page_renders_latest_markdown(client, monkeypatch):
    s3_client = FakeS3Client(
        {
            ("stormy-ai-files", "latest.txt"): "s3://reports/daily/latest.md",
            ("reports", "daily/latest.md"): "# Today's report\n\n**Storms expected.**",
        }
    )
    monkeypatch.setattr(
        "app.stormy_ai.views.boto3.client", lambda service_name: s3_client
    )

    response = client.get("/stormy-ai/")

    assert response.status_code == 200
    assert b"<h1>Today's report</h1>" in response.data
    assert b"<strong>Storms expected.</strong>" in response.data
    assert b"This briefing is a scheduled, AI-written weather analysis" in response.data
    assert b"How Stormy AI Works" in response.data
    assert b'href="/stormy-ai/about/"' in response.data
    assert b'href="/stormy-ai/"' in response.data


def test_render_markdown_removes_executable_html():
    rendered = str(
        render_markdown(
            """# Safe heading

<script>alert('unsafe')</script>
<img src="https://example.com/radar.png" alt="Radar" onerror="alert(1)">
[unsafe link](javascript:alert(1))
"""
        )
    )

    assert "<h1>Safe heading</h1>" in rendered
    assert '<img src="https://example.com/radar.png" alt="Radar">' in rendered
    assert "<script" not in rendered
    assert "onerror" not in rendered
    assert "javascript:" not in rendered


def test_stormy_ai_about_page(client):
    response = client.get("/stormy-ai/about/")

    assert response.status_code == 200
    assert b"How Stormy AI turns raw weather data into a scheduled briefing" in response.data
    assert b"get_mrms_precipitation" in response.data
    assert b"diagnose_precipitation" in response.data
    assert b"The language model can decide when to call those tools" in response.data
    assert b"not the OpenAI API" in response.data
    assert b"Choosing the model for a long, tool-heavy weather run" in response.data
    assert b"zai-org/GLM-5.3-Flash:baseten" in response.data
    assert b"stormy_ai_aws_architecture.svg" in response.data
    assert b"https://github.com/bvmcode/stormy_ai" in response.data
    assert b'href="/stormy-ai/about/"' in response.data
