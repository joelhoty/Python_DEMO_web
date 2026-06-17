import os
import tempfile
import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def test_db_path(tmp_path):
    """Return a temporary database path for isolated test runs."""
    return str(tmp_path / "test.db")


@pytest.fixture
def client(test_db_path):
    """Return a TestClient with an isolated test database."""
    os.environ["DATABASE_URL"] = test_db_path
    from app.main import app
    from app import database
    database.init_db(test_db_path)
    with TestClient(app) as c:
        yield c
    os.environ.pop("DATABASE_URL", None)
