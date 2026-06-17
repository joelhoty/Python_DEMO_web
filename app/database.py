import sqlite3
import os
from datetime import datetime, UTC

DEFAULT_DB = os.path.join(os.path.dirname(__file__), "..", "teaching.db")


def get_db_path() -> str:
    return os.environ.get("DATABASE_URL", DEFAULT_DB)


def get_connection(db_path: str | None = None) -> sqlite3.Connection:
    path = db_path or get_db_path()
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(db_path: str | None = None) -> None:
    """Create the users table if it does not yet exist."""
    conn = get_connection(db_path)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            username    TEXT    NOT NULL UNIQUE,
            password_hash TEXT  NOT NULL,
            created_at  TEXT    NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def create_user(username: str, password_hash: str, db_path: str | None = None) -> int:
    """Insert a new user and return the new row id."""
    conn = get_connection(db_path)
    cur = conn.execute(
        "INSERT INTO users (username, password_hash, created_at) VALUES (?, ?, ?)",
        (username, password_hash, datetime.now(UTC).isoformat()),
    )
    conn.commit()
    user_id = cur.lastrowid
    conn.close()
    return user_id


def get_user_by_username(username: str, db_path: str | None = None) -> sqlite3.Row | None:
    conn = get_connection(db_path)
    row = conn.execute(
        "SELECT * FROM users WHERE username = ?", (username,)
    ).fetchone()
    conn.close()
    return row


def get_user_by_id(user_id: int, db_path: str | None = None) -> sqlite3.Row | None:
    conn = get_connection(db_path)
    row = conn.execute(
        "SELECT * FROM users WHERE id = ?", (user_id,)
    ).fetchone()
    conn.close()
    return row


def update_password(username: str, new_hash: str, db_path: str | None = None) -> None:
    conn = get_connection(db_path)
    conn.execute(
        "UPDATE users SET password_hash = ? WHERE username = ?",
        (new_hash, username),
    )
    conn.commit()
    conn.close()
