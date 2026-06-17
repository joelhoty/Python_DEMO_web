# Project Overview

Generated from `docs/project_notes/` on 2026-06-17 17:16.

## 發展時間軸

- 2026-06-16 17:05 — `issue-001`: FastAPI teaching site proposal prepared; implementation pending approval.
- 2026-06-16 17:05 — `research-001`: Beginner backend teaching scope confirmed.
- 2026-06-16 17:05 — `adr-001`: Build a beginner-focused FastAPI teaching demo.
- 2026-06-16 17:05 — `adr-002`: Use minimal dependencies and standard-library SQLite/hashing.
- 2026-06-16 17:05 — `adr-003`: Make teaching pages interactive and self-explaining.
- 2026-06-16 17:05 — `adr-004`: Include password change, logged-in user creation, and final summary as core scope.
- 2026-06-16 17:05 — `fact-001`: Active OpenSpec change is `create-fastapi-teaching-site`.
- 2026-06-16 17:05 — `fact-002`: Planned Python environment uses `uv`.
- 2026-06-16 17:05 — `fact-003`: Planned package set is intentionally small.
- 2026-06-16 17:05 — `fact-004`: `CLAUDE.md` and `AGENTS.md` provide shared agent guidance.
- 2026-06-16 17:40 — `fact-005`: Verified commands and dependency details.
- 2026-06-16 17:39 — `issue-002`: README expanded and dependency metadata corrected.
- 2026-06-16 17:49 — `research-002`: README teaching explanations refined for FastAPI/Uvicorn, SQLite placeholders, tuple syntax, and salted password hashes.
- 2026-06-16 17:49 — `fact-006`: README now includes concrete beginner examples for request serving layers, SQL parameter binding, and password hash storage format.
- 2026-06-17 17:16 — `issue-003`: Repository branches consolidated so only `main` remains.
- 2026-06-17 17:16 — `fact-007`: Canonical repository branch is now `main`.

## 核心設計決策

- Use a server-rendered FastAPI demo for beginner backend teaching.
- Use `uv` with a small dependency set.
- Use standard-library `sqlite3` for database examples.
- Use standard-library `hashlib` and `secrets` for password hashing.
- Use a teaching cookie for login state, clearly documented as non-production auth.
- Make each teaching page interactive and self-explaining.
- Include password change and logged-in user creation before a final summary.

## 最近修復的 Bug

- No bugs recorded yet.

## 進行中工作

- No active work logged. Current implementation is preserved on `main` and extra branches have been removed.

## 未解決研究問題

- None currently recorded as open.

## 專案基本事實

- Proposal path: `openspec/changes/create-fastapi-teaching-site/`
- Python target: 3.12 or newer
- Environment manager: `uv`
- Install command: `uv sync --dev`
- Server command: `uv run uvicorn app.main:app --reload`
- Test command: `uv run pytest`
- Runtime packages: `fastapi`, `uvicorn[standard]`, `jinja2`, `python-multipart`
- Test packages: `pytest`, `httpx`
- Standard-library modules: `sqlite3`, `hashlib`, `secrets`
- Agent guidance files: `CLAUDE.md`, `AGENTS.md`
- Test status: `uv run pytest` passes 39 tests
- README status: expanded Chinese teaching README aligned with `plan.md`
- README explanation additions: FastAPI/Uvicorn hierarchy, SQL `?` placeholder binding, one-item tuple syntax, `alice` query example, and `salt$hash_hex` as hash storage format
- Canonical branch: `main`
