"""Tests for user registration, password hashing, login, logout, and protected page."""
import pytest
from app import database
from app.auth import hash_password, verify_password


# ---------------------------------------------------------------------------
# Unit tests for auth helpers
# ---------------------------------------------------------------------------

def test_hash_password_is_not_plaintext():
    hashed = hash_password("mysecret")
    assert "mysecret" not in hashed


def test_verify_password_correct():
    hashed = hash_password("correcthorse")
    assert verify_password("correcthorse", hashed) is True


def test_verify_password_wrong():
    hashed = hash_password("correcthorse")
    assert verify_password("wrongpassword", hashed) is False


def test_hash_contains_salt_separator():
    hashed = hash_password("test")
    assert "$" in hashed


# ---------------------------------------------------------------------------
# Integration tests for registration routes
# ---------------------------------------------------------------------------

def test_register_page_loads(client):
    response = client.get("/register")
    assert response.status_code == 200
    assert b"<form" in response.content


def test_register_creates_user(client, test_db_path):
    import os
    db_path = os.environ.get("DATABASE_URL", test_db_path)
    response = client.post(
        "/register",
        data={"username": "newuser", "password": "pass1234"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    user = database.get_user_by_username("newuser", db_path=db_path)
    assert user is not None


def test_register_hashes_password(client, test_db_path):
    import os
    db_path = os.environ.get("DATABASE_URL", test_db_path)
    client.post(
        "/register",
        data={"username": "hashtest", "password": "plaintext"},
        follow_redirects=True,
    )
    user = database.get_user_by_username("hashtest", db_path=db_path)
    assert user is not None
    assert "plaintext" not in user["password_hash"]
    assert "$" in user["password_hash"]


def test_register_duplicate_username(client):
    client.post("/register", data={"username": "dup", "password": "pass1"})
    response = client.post(
        "/register",
        data={"username": "dup", "password": "pass2"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"already" in response.content.lower() or b"exist" in response.content.lower() or b"error" in response.content.lower()


# ---------------------------------------------------------------------------
# Login / logout / protected page
# ---------------------------------------------------------------------------

def _register_and_login(client, username="testuser", password="testpass"):
    """Helper: register a user and log in, return the login response."""
    client.post("/register", data={"username": username, "password": password})
    return client.post(
        "/login",
        data={"username": username, "password": password},
        follow_redirects=True,
    )


def test_login_page_loads(client):
    response = client.get("/login")
    assert response.status_code == 200
    assert b"<form" in response.content


def test_successful_login_redirects_to_protected(client):
    client.post("/register", data={"username": "loginok", "password": "secret"})
    response = client.post(
        "/login",
        data={"username": "loginok", "password": "secret"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    # Should end up on protected page or a page that shows the username
    assert b"loginok" in response.content or b"protected" in response.content.lower()


def test_failed_login_shows_error(client):
    client.post("/register", data={"username": "failuser", "password": "correct"})
    response = client.post(
        "/login",
        data={"username": "failuser", "password": "wrong"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    content = response.content.lower()
    assert b"invalid" in content or b"error" in content or b"incorrect" in content


def test_anonymous_protected_redirects_to_login(client):
    response = client.get("/protected", follow_redirects=False)
    assert response.status_code in (302, 303)
    assert "/login" in response.headers.get("location", "")


def test_logged_in_protected_page(client):
    resp = _register_and_login(client, "protuser", "secret123")
    assert resp.status_code == 200
    assert b"protuser" in resp.content or b"protected" in resp.content.lower()


def test_logout_clears_session(client):
    _register_and_login(client, "logoutuser", "pass")
    logout_resp = client.post("/logout", follow_redirects=True)
    assert logout_resp.status_code == 200
    # After logout, protected should redirect again
    protected = client.get("/protected", follow_redirects=False)
    assert protected.status_code in (302, 303)


# ---------------------------------------------------------------------------
# Password change
# ---------------------------------------------------------------------------

def _logged_in_client(client, username="pwuser", password="oldpass"):
    """Register and log in; return (client, username, password)."""
    client.post("/register", data={"username": username, "password": password})
    client.post("/login", data={"username": username, "password": password})
    return username, password


def test_change_password_page_requires_login(client):
    response = client.get("/change-password", follow_redirects=False)
    assert response.status_code in (302, 303)
    assert "/login" in response.headers.get("location", "")


def test_change_password_success(client, test_db_path):
    import os
    db_path = os.environ.get("DATABASE_URL", test_db_path)
    username, old_pass = _logged_in_client(client, "chpwuser", "oldpassword")
    response = client.post(
        "/change-password",
        data={"current_password": old_pass, "new_password": "newpassword123"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    # Verify new password works
    user = database.get_user_by_username(username, db_path=db_path)
    assert verify_password("newpassword123", user["password_hash"])


def test_change_password_wrong_current(client):
    _logged_in_client(client, "wrongpwuser", "correct")
    response = client.post(
        "/change-password",
        data={"current_password": "wrong", "new_password": "newpass"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    content = response.content.lower()
    assert b"incorrect" in content or b"wrong" in content or b"error" in content


# ---------------------------------------------------------------------------
# Authenticated user creation (add-user)
# ---------------------------------------------------------------------------

def test_add_user_page_requires_login(client):
    response = client.get("/add-user", follow_redirects=False)
    assert response.status_code in (302, 303)
    assert "/login" in response.headers.get("location", "")


def test_add_user_success(client, test_db_path):
    import os
    db_path = os.environ.get("DATABASE_URL", test_db_path)
    _logged_in_client(client, "creator", "createpass")
    response = client.post(
        "/add-user",
        data={"username": "newcreated", "password": "created123"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    user = database.get_user_by_username("newcreated", db_path=db_path)
    assert user is not None
    assert "created123" not in user["password_hash"]


def test_add_user_anonymous_rejected(client):
    response = client.post(
        "/add-user",
        data={"username": "anon_attempt", "password": "pass"},
        follow_redirects=False,
    )
    assert response.status_code in (302, 303)
    assert "/login" in response.headers.get("location", "")

