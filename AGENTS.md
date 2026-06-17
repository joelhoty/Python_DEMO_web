# Agent Guidance

## Project Memory System

This project maintains shared project memory in `docs/project_notes/`.
Agents should read relevant memory before proposing or implementing changes.

### Memory Files

- `docs/project_notes/OVERVIEW.md` - Current project briefing and timeline
- `docs/project_notes/decisions.md` - Decision index
- `docs/project_notes/decisions/` - Split-file ADR entries
- `docs/project_notes/research.md` - Research and planning discussion history
- `docs/project_notes/key_facts.md` - Stable project facts, commands, and non-secret configuration
- `docs/project_notes/issues.md` - Work log
- `docs/project_notes/bugs.md` - Bug log

### Protocol

- Before proposing architecture or dependency changes, check `decisions.md`, `decisions/`, and `research.md`.
- Before assuming commands or project setup, check `key_facts.md`.
- When completing significant work, update `issues.md` and regenerate `OVERVIEW.md`.
- When making or revising architectural choices, add a structured ADR entry under `docs/project_notes/decisions/`.
- Do not store secrets, tokens, or real passwords in memory files.
- New memory entries should use YAML front matter and `YYYY-MM-DD HH:MM` timestamps.

## OpenSpec Workflow

- Active proposal: `openspec/changes/create-fastapi-teaching-site/`
- Do not implement application code until the proposal is approved.
- If implementation begins, follow `tasks.md` and keep the work aligned with `proposal.md`, `design.md`, and `specs/teaching-site/spec.md`.

## Current Project Direction

Build a beginner-focused FastAPI teaching website.

Core direction:

- Server-rendered FastAPI pages using Jinja2.
- Minimal dependency set managed by `uv`.
- SQLite examples through Python standard-library `sqlite3`.
- Password hashing through Python standard-library `hashlib` and `secrets`.
- Teaching-cookie login state, documented as a teaching simplification rather than production auth.
- Interactive pages that combine concept explanation, operation, result, and "what happened" notes.
- Core lesson includes GET/POST comparison, forms, database operations, registration, login, protected page, password change, logged-in user creation, commercial stack overview, and final summary.

## Planned Commands

- Install dependencies: `uv sync --dev`
- Run server: `uv run uvicorn app.main:app --reload`
- Run tests: `uv run pytest`
