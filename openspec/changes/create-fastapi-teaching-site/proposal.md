# Proposal: Create FastAPI Teaching Site

## Why
The project needs a small, runnable teaching website that explains core backend and web concepts through working examples. The current workspace has no application structure, so learners do not yet have a concrete place to see how browser forms, HTTP methods, variable passing, database operations, and basic account handling fit together.

## What
This change will add a FastAPI-based teaching site for introducing:

- Backend route design and the role of the web backend
- GET routes for pages, path parameters, and query parameters
- POST routes for HTML form submission
- Practical differences between GET and POST variable passing
- A dedicated interactive GET/POST page where learners submit the same kind of value through both methods and compare the visible differences
- URL-based variable passing and receiving values on the backend
- Form data handling with FastAPI
- Dedicated interactive concept pages for forms and database operations using the same pattern: concept explanation, hands-on operation, and result explanation
- In-page explanations so learners can use the demo site while seeing what each page, route, method, and data flow is demonstrating
- Frontend, backend, and database integration through one demo architecture
- A short comparison of real commercial frontend/backend/database/server stacks
- SQLite-backed user storage
- Basic user registration and login
- Password hashing instead of plaintext password storage
- Protected pages that require a logged-in user
- Authenticated password change
- Authenticated creation of another user account
- A final summary page that closes the lesson after account-management examples

This change will not add production-grade account recovery, email verification, OAuth, deployment automation, or advanced role-based authorization.

## `plan.md` Highlights
The proposal incorporates the teaching points from `plan.md`:

1. FastAPI route design as the concrete example of what a backend does.
2. GET and POST examples that show practical differences in variable passing.
3. URL variable transfer through query parameters and path parameters.
4. Form-based variable transfer through POST form data.
5. Frontend-backend-database wiring, including the demo architecture and key functions used.
6. A beginner-level explanation of how commercial frontend, backend, database, and server choices fit together.
7. A virtual teaching database with users and passwords.
8. User login implementation and explanation.
9. Logged-in password change implementation and explanation.
10. Logged-in creation of another user and password implementation and explanation.

## How
The site will use FastAPI, Jinja2 templates, static assets, SQLite through Python's standard-library `sqlite3`, password hashing through Python's standard-library `hashlib` and `secrets`, and a simple teaching cookie for login state. Pages will be intentionally simple and instructional, with each route showing a concrete concept while still forming one coherent mini website.

The project will use `uv` for virtual environment and dependency management. Runtime and test dependencies will be declared in `pyproject.toml`, installed into a local `.venv` with `uv sync`, and executed with `uv run`. The first implementation will prefer clarity over framework layering so students can read the full request-to-database flow in a small number of files.

## Python Environment And Library Plan
Environment:

- Python target: Python 3.12 or newer
- Virtual environment: `.venv` managed by `uv`
- Dependency file: `pyproject.toml`
- Lock file: `uv.lock`
- Install command: `uv sync --dev`
- Run server command: `uv run uvicorn app.main:app --reload`
- Run tests command: `uv run pytest`

Runtime libraries:

- `fastapi`: web framework, routes, request handling, dependency injection
- `uvicorn[standard]`: ASGI development server
- `jinja2`: server-rendered HTML templates
- `python-multipart`: HTML form parsing for FastAPI `Form(...)`

Development and test libraries:

- `pytest`: automated tests
- `httpx`: test client transport dependency for FastAPI/Starlette testing

Standard-library modules used intentionally for teaching:

- `sqlite3`: database connection, table creation, insert, select, and update examples
- `hashlib`: PBKDF2 password hashing
- `secrets`: random salt generation and constant-time hash comparison support

SQLite will not require a separate database server or third-party ORM. This keeps the demo closer to the raw concepts: SQL table creation, parameterized queries, and rows returned from the database.

## Impact
Expected new areas include:

- `app/main.py` for FastAPI routes and application setup
- `app/database.py` for SQLite connection setup and small query helper functions
- `app/auth.py` for password hashing and login helpers
- `app/templates/` for HTML pages and forms
- `app/static/` for CSS
- `tests/` for route, form, database, and authentication behavior
- `pyproject.toml` and `uv.lock` for `uv`-managed dependencies
- `.python-version` to pin the local Python version for `uv`

## Simplified Scope For Beginners
The core lesson should be finishable in limited time:

- Core: route design, GET, POST, URL variables, form variables, SQLite users table, registration, login, protected page, and commercial stack overview.
- Core pages should be self-explaining and interactive: while using each demo page, the learner should see which route is being used, which HTTP method is involved, what data is sent, what changed on screen, and what backend/database action happens.
- Concept pages should follow the same teaching structure: short explanation, input controls, submit action, rendered result, and a concise "what happened" section.
- Account-management close: logged-in password change, logged-in creation of another user, and a final summary that reviews the full browser-to-backend-to-database flow.

The lesson intentionally stops after password change and logged-in user creation, because that gives learners a complete small account-management flow without moving into production authentication features.

## Risks
The main risk is accidentally teaching insecure password practices. The mitigation is to require password hashing from the first implementation while clearly labeling the cookie login as a teaching simplification rather than production authentication. Another risk is overbuilding the site; the implementation should stay focused on beginner-visible backend concepts and avoid production features that distract from GET, POST, forms, variables, and database CRUD. A third risk is dependency confusion for beginners; using only a few external packages and relying on standard-library SQLite and hashing keeps the workflow easier to explain.
