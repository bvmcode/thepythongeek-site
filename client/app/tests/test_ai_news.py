from app.hermes.views import get_ai_news_markdown


def test_get_ai_news_markdown_reads_daily_file():
    assert get_ai_news_markdown().strip()


def test_ai_news_page_renders_markdown_file(client, monkeypatch):
    monkeypatch.setattr(
        "app.hermes.views.get_ai_news_markdown",
        lambda: "# Monday briefing\n\n**OpenAI** signed a deal.",
    )

    response = client.get("/ai-news/")

    assert response.status_code == 200
    assert b"<h1>Monday briefing</h1>" in response.data
    assert b"<strong>OpenAI</strong>" in response.data
    assert b'href="/ai-news/"' in response.data


def test_ai_news_page_handles_missing_file(client, monkeypatch):
    def missing():
        raise FileNotFoundError("ai_news.md")

    monkeypatch.setattr("app.hermes.views.get_ai_news_markdown", missing)

    response = client.get("/ai-news/")

    assert response.status_code == 503
    assert b"temporarily unavailable" in response.data
