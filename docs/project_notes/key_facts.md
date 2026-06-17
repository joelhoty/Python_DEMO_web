# Key Facts

Project facts and stable configuration. Do not store secrets, tokens, or real passwords here.

---
id: fact-001
timestamp: 2026-06-16 17:05
type: fact
tags: [project, openspec]
component: planning
source: openspec/changes/create-fastapi-teaching-site
change: create-fastapi-teaching-site
---

## Fact-001: Active Change Proposal

- Change name: `create-fastapi-teaching-site`
- Proposal directory: `openspec/changes/create-fastapi-teaching-site/`
- Current status: proposal active, implementation not started
- Git repository initialized on 2026-06-16

---
id: fact-002
timestamp: 2026-06-16 17:05
type: fact
tags: [python, uv, dependencies]
component: project-setup
source: openspec/changes/create-fastapi-teaching-site
change: create-fastapi-teaching-site
---

## Fact-002: Planned Python Environment

- Python target: 3.12 or newer
- Environment manager: `uv`
- Dependency file: `pyproject.toml`
- Lock file: `uv.lock`
- Install command: `uv sync --dev`
- Run server command: `uv run uvicorn app.main:app --reload`
- Run tests command: `uv run pytest`

---
id: fact-003
timestamp: 2026-06-16 17:05
type: fact
tags: [dependencies, teaching]
component: project-setup
source: openspec/changes/create-fastapi-teaching-site
change: create-fastapi-teaching-site
---

## Fact-003: Planned Library Set

- Runtime packages: `fastapi`, `uvicorn[standard]`, `jinja2`, `python-multipart`
- Test packages: `pytest`, `httpx`
- Standard-library teaching modules: `sqlite3`, `hashlib`, `secrets`
- Explicitly avoided for the first version: SQLAlchemy, JWT, OAuth, production session middleware, and advanced auth frameworks

---
id: fact-004
timestamp: 2026-06-16 17:05
type: fact
tags: [agents, memory, guidance]
component: project-guidance
source: docs/project_notes
---

## Fact-004: Agent Guidance Files

- `CLAUDE.md` exists for Claude-style project guidance.
- `AGENTS.md` exists for Codex, Cursor, Copilot CLI, and other agent workflows.
- Both guidance files point agents to `docs/project_notes/` before making architecture or implementation decisions.

---
id: fact-005
timestamp: 2026-06-16 17:40
type: fact
tags: [python, uv, dependencies, verified]
component: project-setup
source: pyproject.toml
change: create-fastapi-teaching-site
---

## Fact-005: Verified Commands And Dependency Details

- Install: `uv sync --dev`
- Run server: `uv run uvicorn app.main:app --reload` (default port 8000)
- Run tests: `uv run pytest` (39 tests, ~1s)
- Test packages use `httpx`
- Starlette 1.x `TemplateResponse` API: `templates.TemplateResponse(request, "name.html", {"key": val})`
- SQLite database file: `teaching.db` in project root (excluded from git via .gitignore)
- Test database: isolated per-test via `DATABASE_URL` env var in `tests/conftest.py`
- Feature branch: `feat/create-fastapi-teaching-site`
- Cookie name for teaching login state: `teaching_user`

---
id: fact-006
timestamp: 2026-06-16 17:49
type: fact
tags: [readme, teaching, sqlite, auth, fastapi]
component: documentation
source: README.md
change: create-fastapi-teaching-site
---

## Fact-006: README Teaching Explanation Additions

- README includes a FastAPI/Uvicorn layering section: Uvicorn listens as the ASGI server; FastAPI routes and handles application logic.
- README explains SQLite `?` placeholders as parameter binding, not SQL string replacement.
- README includes the concrete `username = "alice"` example with params `("alice",)` and explains why SQL does not become `('alice',)`.
- README explains that one-item tuples require the trailing comma: `(username,)`.
- README clarifies `salt$hash_hex` is this demo's storage format for a salted password hash, not encryption and not a special standard term.

---
id: fact-007
timestamp: 2026-06-17 17:16
type: fact
tags: [git, github, branches]
component: repository-management
source: git
---

## Fact-007: Canonical Branch Is Main

- Repository branch policy is consolidated to `main`.
- Extra local and GitHub branches were removed after preserving the latest teaching-site work on `main`.
- `origin/HEAD` should resolve to `origin/main`.
