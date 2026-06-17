import pytest


def test_home_page_returns_html(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert b"FastAPI" in response.content or b"Teaching" in response.content
