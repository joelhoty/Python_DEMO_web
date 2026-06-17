"""Tests for teaching pages: GET/POST comparison, form, search, commercial stack."""
import pytest


def test_methods_page(client):
    response = client.get("/methods")
    assert response.status_code == 200
    assert b"GET" in response.content
    assert b"POST" in response.content


def test_methods_get_demo(client):
    response = client.get("/methods/get-demo?message=hello")
    assert response.status_code == 200
    assert b"hello" in response.content
    # URL/query-string explanation should be present
    assert b"URL" in response.content or b"query" in response.content.lower()


def test_methods_post_demo(client):
    response = client.post("/methods/post-demo", data={"message": "world"})
    assert response.status_code == 200
    assert b"world" in response.content
    # Body/request explanation should be present
    assert b"body" in response.content.lower() or b"POST" in response.content


def test_search_page(client):
    response = client.get("/search?q=fastapi")
    assert response.status_code == 200
    assert b"fastapi" in response.content


def test_form_get_page(client):
    response = client.get("/form")
    assert response.status_code == 200
    assert b"<form" in response.content


def test_form_post(client):
    response = client.post("/form", data={"name": "Alice", "message": "Hi"})
    assert response.status_code == 200
    assert b"Alice" in response.content
    assert b"Hi" in response.content


def test_commercial_stack_page(client):
    response = client.get("/commercial-stack")
    assert response.status_code == 200
    # Page should mention several real technologies
    content = response.content.lower()
    assert b"react" in content or b"vue" in content or b"angular" in content
    assert b"django" in content or b"node" in content or b"rails" in content


def test_methods_page_explains_difference(client):
    """The methods page should explain GET vs POST difference."""
    response = client.get("/methods")
    content = response.content.lower()
    assert b"url" in content
    assert b"body" in content or b"form" in content


def test_methods_get_demo_value_in_url_explanation(client):
    """GET demo page should explain that value appeared in the URL."""
    response = client.get("/methods/get-demo?message=testval")
    content = response.content
    assert b"testval" in content


def test_methods_post_demo_value_not_in_url(client):
    """POST demo result should contain submitted value but not as URL parameter."""
    response = client.post("/methods/post-demo", data={"message": "secret"})
    assert b"secret" in response.content


def test_summary_page(client):
    response = client.get("/summary")
    assert response.status_code == 200
    content = response.content.lower()
    # Should mention the key lesson topics
    assert b"get" in content
    assert b"post" in content
    assert b"database" in content or b"sqlite" in content
    assert b"password" in content
    assert b"login" in content or b"session" in content or b"cookie" in content
