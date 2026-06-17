"""Tests for database operations and user model."""
import pytest
from app import database


def test_database_init_creates_users_table(test_db_path):
    database.init_db(test_db_path)
    conn = database.get_connection(test_db_path)
    tables = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='users'"
    ).fetchone()
    conn.close()
    assert tables is not None


def test_create_user(test_db_path):
    database.init_db(test_db_path)
    uid = database.create_user("alice", "hash123", db_path=test_db_path)
    assert uid is not None and uid > 0


def test_get_user_by_username(test_db_path):
    database.init_db(test_db_path)
    database.create_user("bob", "hash456", db_path=test_db_path)
    user = database.get_user_by_username("bob", db_path=test_db_path)
    assert user is not None
    assert user["username"] == "bob"


def test_get_user_by_id(test_db_path):
    database.init_db(test_db_path)
    uid = database.create_user("charlie", "hash789", db_path=test_db_path)
    user = database.get_user_by_id(uid, db_path=test_db_path)
    assert user is not None
    assert user["username"] == "charlie"


def test_database_concept_page(client):
    response = client.get("/database")
    assert response.status_code == 200
    assert b"database" in response.content.lower() or b"Database" in response.content


def test_user_lookup_by_id(client, test_db_path):
    import os
    db_path = os.environ.get("DATABASE_URL", test_db_path)
    uid = database.create_user("dave", "dummyhash", db_path=db_path)
    response = client.get(f"/users/{uid}")
    assert response.status_code == 200
    assert b"dave" in response.content


def test_user_lookup_unknown_id(client):
    response = client.get("/users/99999")
    assert response.status_code in (200, 404)
    if response.status_code == 200:
        assert b"not found" in response.content.lower() or b"404" in response.content
