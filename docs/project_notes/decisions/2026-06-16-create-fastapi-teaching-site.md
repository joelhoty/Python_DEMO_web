---
id: adr-001
timestamp: 2026-06-16 17:05
type: decision
tags: [fastapi, teaching, architecture]
component: teaching-site
source: openspec/changes/create-fastapi-teaching-site
change: create-fastapi-teaching-site
---

## ADR-001: Build A Beginner-Focused FastAPI Teaching Demo

**Context:**
- The project is intended to introduce backend and website concepts to beginners using Python and FastAPI.
- The demo must be usable during teaching, not only read as documentation.

**Decision:**
- Build a small server-rendered FastAPI website covering route design, GET/POST, URL variables, forms, SQLite database operations, registration, login, password change, logged-in user creation, and a final summary.

**Alternatives Considered:**
- API-only backend -> Rejected because beginners need to see forms and browser behavior directly.
- Full frontend/backend split -> Rejected because it adds too much setup for the available time.

**Consequences:**
- The app remains close to the browser-to-backend-to-database flow.
- It can be demonstrated live while learners read concise page-level explanations.

---
id: adr-002
timestamp: 2026-06-16 17:05
type: decision
tags: [dependencies, sqlite, auth, uv]
component: project-setup
source: openspec/changes/create-fastapi-teaching-site
change: create-fastapi-teaching-site
---

## ADR-002: Use Minimal Dependencies And Standard-Library SQLite/Hashing

**Context:**
- The original proposal included more framework layering, but the user clarified that time is limited and the audience is beginner-level.

**Decision:**
- Use `uv` for the environment, with a small package set: `fastapi`, `uvicorn[standard]`, `jinja2`, `python-multipart`, `pytest`, and `httpx`.
- Use Python standard-library `sqlite3` for database examples.
- Use Python standard-library `hashlib` and `secrets` for teaching password hashing.
- Use a simple teaching cookie for login state, clearly documented as not production authentication.

**Alternatives Considered:**
- SQLAlchemy -> Rejected for first version because raw SQL is more transparent for teaching database concepts.
- Third-party password libraries -> Deferred because standard-library PBKDF2 is adequate for a teaching demo with fewer moving parts.
- JWT or full session middleware -> Rejected for first version because it distracts from the core login concept.

**Consequences:**
- Learners can see SQL table creation, parameterized queries, and password hashing without extra abstraction.
- Documentation must clearly separate teaching simplifications from production security patterns.

---
id: adr-003
timestamp: 2026-06-16 17:05
type: decision
tags: [ux, teaching, interaction]
component: templates
source: openspec/changes/create-fastapi-teaching-site
change: create-fastapi-teaching-site
---

## ADR-003: Make Teaching Pages Interactive And Self-Explaining

**Context:**
- The user requested that learners should be able to operate the demo site and understand each page's function from the page content itself.

**Decision:**
- Core pages will follow a repeated teaching pattern: concept explanation, input controls, submit action, rendered result, and a "what happened" explanation.
- Dedicated pages will exist for GET/POST comparison, forms, database operations, and account-management flows.

**Alternatives Considered:**
- Static explanatory pages -> Rejected because they do not show request/response behavior.
- Hidden explanations only in README -> Rejected because the demo should be understandable while being used.

**Consequences:**
- Pages need compact concept panels showing route, method, data source, backend action, and database action when relevant.
- Tests should verify both behavior and important explanation content.

---
id: adr-004
timestamp: 2026-06-16 17:05
type: decision
tags: [auth, scope, teaching]
component: account-management
source: openspec/changes/create-fastapi-teaching-site
change: create-fastapi-teaching-site
---

## ADR-004: Include Password Change, Logged-In User Creation, And Summary As Core Scope

**Context:**
- `plan.md` includes logged-in password change and logged-in creation of another user.
- The user clarified these should be included and used as the point where the lesson concludes.

**Decision:**
- Include `/change-password`, `/add-user`, and `/summary` in the core scope.
- The summary page closes the lesson by reviewing GET/POST, forms, database reads/writes, password hashing, login state, password change, and logged-in user creation.

**Alternatives Considered:**
- Treat these as optional extensions -> Rejected after user clarified they should be included.

**Consequences:**
- The demo has a complete small account-management arc.
- Scope stops before production account recovery, OAuth, email verification, deployment automation, or advanced authorization.
