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

---
id: issue-003
timestamp: 2026-06-17 17:16
type: issue
tags: [git, github, branches, maintenance]
severity: low
component: repository-management
status: resolved
source: git
---

## Issue-003: Consolidate repository onto main only

- Synced remote refs from GitHub and audited branch divergence before cleanup.
- Confirmed `feat/create-fastapi-teaching-site` contained the latest teaching-site work not yet reflected on `origin/main`.
- Repointed local and remote `main` to the latest teaching-site commit so the work is preserved on the canonical branch.
- Removed extra local and remote branches to leave `main` as the only remaining branch.
