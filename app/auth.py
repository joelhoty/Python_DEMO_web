import hashlib
import os
import secrets
from typing import Optional

from fastapi import Cookie, Request
from fastapi.responses import RedirectResponse

from app import database


def hash_password(password: str) -> str:
    """Return a salted PBKDF2-HMAC-SHA256 hash string."""
    salt = secrets.token_hex(16)
    dk = hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), 260_000)
    return f"{salt}${dk.hex()}"


def verify_password(password: str, stored_hash: str) -> bool:
    """Return True if *password* matches *stored_hash*."""
    try:
        salt, dk_hex = stored_hash.split("$", 1)
    except ValueError:
        return False
    dk = hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), 260_000)
    return secrets.compare_digest(dk.hex(), dk_hex)


# ---------------------------------------------------------------------------
# Teaching-cookie helpers
# ---------------------------------------------------------------------------
COOKIE_NAME = "teaching_user"


def get_current_user(request: Request) -> Optional[str]:
    """Return the username stored in the teaching cookie, or None."""
    return request.cookies.get(COOKIE_NAME)


def require_login(request: Request) -> Optional[RedirectResponse]:
    """Return a redirect to /login if not logged in, else None."""
    if not get_current_user(request):
        return RedirectResponse("/login", status_code=303)
    return None
