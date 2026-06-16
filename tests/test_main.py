import pytest
from httpx2 import ASGITransport, AsyncClient

from app.main import app


@pytest.fixture
async def client():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        yield ac


async def test_home_status(client):
    response = await client.get("/")
    assert response.status_code == 200


async def test_home_content(client):
    response = await client.get("/")
    assert "Welcome to Python Demo Web!" in response.text
    assert "Home" in response.text


async def test_about_status(client):
    response = await client.get("/about")
    assert response.status_code == 200


async def test_about_content(client):
    response = await client.get("/about")
    assert "About" in response.text
    assert "FastAPI" in response.text
