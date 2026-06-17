# Issues / Work Log

Project work log. Each future entry should use YAML front matter with `type: issue`.

---
id: issue-001
timestamp: 2026-06-16 17:05
type: issue
tags: [planning, openspec, teaching-site]
severity: low
component: planning
status: resolved
source: openspec/changes/create-fastapi-teaching-site
change: create-fastapi-teaching-site
---

## Issue-001: FastAPI teaching site proposal prepared

- Created OpenSpec proposal artifacts for the beginner FastAPI teaching site.
- Scope now includes interactive GET/POST, form, database, registration, login, password change, logged-in user creation, commercial stack overview, and final summary.
- Implementation has since been completed and verified.

---
id: issue-002
timestamp: 2026-06-16 17:39
type: issue
tags: [documentation, readme, dependencies]
severity: low
component: documentation
status: resolved
source: README.md
change: create-fastapi-teaching-site
---

## Issue-002: README expanded and dev dependency corrected

- Rewrote `README.md` into a detailed Chinese teaching document aligned with `plan.md`.
- Added a dedicated explanation of FastAPI vs Uvicorn layering and request flow.
- Added detailed SQLite placeholder, one-item tuple, and `alice` parameter binding examples.
- Clarified password storage wording: `salt$hash_hex` is a salted hash storage format, not encryption.
- Corrected development dependency metadata from `httpx2` to `httpx` in `pyproject.toml` and regenerated `uv.lock`.
- Verified with `uv run pytest`: 39 tests passed.
