# Research Log

Research and design discussion history. Entries are grouped by focused session.

## Session 2026-06-16 17:05 — FastAPI Teaching Site Planning

---
id: research-001
timestamp: 2026-06-16 17:05
type: research
tags: [fastapi, teaching, beginner, backend]
component: teaching-site
source: conversation
change: create-fastapi-teaching-site
related: [adr-001, adr-002, adr-003, adr-004]
---

## Research-001: Beginner Backend Teaching Scope

**Question:**
- What should a beginner-friendly Python/FastAPI website demo teach within limited time?

**Context:**
- The initial idea was to introduce backend concepts, websites, forms, GET/POST, variable passing, database operations, and simple user/password management.
- `plan.md` lists 10 teaching points from route design through logged-in password change and logged-in user creation.

**Exploration:**
- Considered a broader FastAPI stack using ORM/session abstractions.
- User clarified that the target is beginner-level and time-limited, so the architecture should be simpler and concept-focused.
- User also clarified that demo pages should be usable while showing the current page's functional explanation.

**Finding:**
- Build a server-rendered FastAPI demo with interactive concept pages. Confidence: Confirmed.
- Use minimal dependencies and standard-library `sqlite3`, `hashlib`, and `secrets` to keep core concepts visible. Confidence: Confirmed.
- Include password change and logged-in user creation as core lesson endpoints, then close with a summary page. Confidence: Confirmed.

**Implications:**
- Implementation should prioritize clear route functions, forms, visible request variables, parameterized SQL examples, and page-level "what happened" explanations.
- Avoid production auth complexity; label the login cookie as a teaching simplification.

**Related:**
- `openspec/changes/create-fastapi-teaching-site/`
- `plan.md`

## Session 2026-06-16 17:49 — README Teaching Explanation Refinement

---
id: research-002
timestamp: 2026-06-16 17:49
type: research
tags: [readme, teaching, fastapi, sqlite, auth]
component: documentation
source: README.md
change: create-fastapi-teaching-site
related: [fact-006, issue-002]
---

## Research-002: Clarify Beginner Explanations In README

**Question:**
- Which explanations should be expanded so beginners can understand the demo without prior backend knowledge?

**Context:**
- The README was expanded from `plan.md`, then the user asked for more detail on FastAPI/Uvicorn responsibilities, SQLite `?` placeholders, Python one-item tuples, and whether `salt$hash_hex` is a special term or encrypted password.

**Exploration:**
- FastAPI and Uvicorn were separated into layers: Uvicorn is the ASGI server that listens for HTTP requests; FastAPI is the web framework that routes requests and calls Python functions.
- SQLite placeholder usage was clarified as "SQL template + parameter tuple", not string replacement and not SQL containing a tuple.
- The one-item tuple syntax `(username,)` was clarified: Python tuple-ness comes from the comma, not the parentheses.
- `salt$hash_hex` was clarified as this demo's storage format for a salted password hash, not a standard term and not encryption.

**Finding:**
- README should prioritize concrete examples over abstract definitions for this beginner audience. Confidence: Confirmed.
- The `alice` example is the preferred explanation for parameter binding: SQL template `SELECT ... username = ?` plus params `("alice",)` conceptually queries username `'alice'` while avoiding string concatenation. Confidence: Confirmed.
- Password wording should use "hash" or "password hash", not "encrypted password". Confidence: Confirmed.

**Implications:**
- Future documentation should keep distinguishing teaching simplifications from production practices.
- Future agents should preserve the FastAPI/Uvicorn layer explanation and SQL placeholder explanation when editing README.

**Related:**
- `README.md`
- `app/database.py`
- `app/auth.py`
