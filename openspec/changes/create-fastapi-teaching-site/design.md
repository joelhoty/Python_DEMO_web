# Design: Create FastAPI Teaching Site

## Architecture
The application will be a small server-rendered FastAPI site. FastAPI will handle routes, Jinja2 will render pages, SQLite will persist users through Python's standard-library `sqlite3`, password hashing will use Python's standard-library `hashlib` and `secrets`, and a simple HTTP-only teaching cookie will store login state.

The data flow is intentionally direct: browser requests an HTML page, user submits a form, FastAPI validates form data, the database layer reads or writes records, and the response renders a template or redirects to another route. Each teaching page will include a compact explanation panel describing the route, HTTP method, incoming variables, backend function, and database action when relevant.

Core teaching pages will follow a repeated pattern:

- Concept: short description of the backend idea.
- Try it: input controls or links that trigger the route.
- Result: values received by the backend and any generated response.
- What happened: concise explanation of URL variables, form body variables, cookie state, or database reads/writes.

The local development environment will be managed by `uv`. Dependencies will be declared in `pyproject.toml`, locked in `uv.lock`, installed into `.venv`, and used through `uv run` for both server execution and tests.

## Components
- `app/main.py`: Creates the FastAPI app, configures templates/static files, and defines teaching routes.
- `app/database.py`: Defines SQLite initialization and small functions for creating users, finding users, and updating passwords.
- `app/auth.py`: Handles standard-library password hashing, password verification, and simple cookie helpers for the demo login state.
- `app/templates/`: Contains base layout, home page, GET/POST comparison page, form concept page, database concept page, search result, user pages, register page, login page, protected page, change-password page, add-user page, commercial stack explanation, and final summary page. Templates should include a small concept panel so the learner can operate the demo and read what the current page is doing.
- `app/static/`: Contains lightweight CSS for readable teaching pages.
- `tests/`: Uses FastAPI `TestClient` and an isolated test database to verify behavior.
- `pyproject.toml`: Declares project metadata, runtime dependencies, development dependencies, and tool settings.
- `.python-version`: Pins the Python version used by `uv`.

## Dependencies
Runtime dependencies:

- `fastapi`: route definitions, request handling, `Form(...)`, dependency injection, and response helpers.
- `uvicorn[standard]`: local ASGI server for `uv run uvicorn app.main:app --reload`.
- `jinja2`: HTML templates for server-rendered pages.
- `python-multipart`: parsing browser form submissions.

Development dependencies:

- `pytest`: automated tests.
- `httpx`: HTTP client support used by FastAPI/Starlette tests.

Standard-library modules:

- `sqlite3`: SQL table creation and parameterized database queries.
- `hashlib`: PBKDF2 password hashing.
- `secrets`: random salts and constant-time comparisons.

## Interfaces
- `GET /`: Home page with links to examples and an overview of backend responsibilities.
- `GET /methods`: Shows the GET/POST comparison page with two interactive examples.
- `GET /methods/get-demo?message=example`: Receives a query string value and renders the GET result.
- `POST /methods/post-demo`: Receives a form body value and renders the POST result.
- `GET /search?q=example`: Demonstrates query parameters and explains that values come from the URL after `?`.
- `GET /users/{user_id}`: Demonstrates path parameters and explains database lookup by id.
- `GET /form`: Shows a form concept page and explains that the browser has not submitted data yet.
- `POST /form`: Reads submitted form values, renders the result, and explains form body data.
- `GET /database`: Shows a database concept page for creating and looking up users.
- `GET /register`: Shows registration form and explains the future database write.
- `POST /register`: Creates a user with a hashed password and explains the database insert.
- `GET /login`: Shows login form and explains the future database read.
- `POST /login`: Verifies credentials, stores demo login state, and explains the database read plus cookie write.
- `POST /logout`: Clears demo login state and explains cookie removal.
- `GET /protected`: Requires login and explains why the cookie is checked before rendering.
- `GET /change-password`: Shows a password change form for the current user.
- `POST /change-password`: Verifies current password and stores a hash for the new password.
- `GET /add-user`: Shows a logged-in-only form for creating another teaching user.
- `POST /add-user`: Creates another user with a hashed password.
- `GET /commercial-stack`: Explains common commercial frontend, backend, database, and server combinations.
- `GET /summary`: Summarizes the lesson after password change and logged-in user creation.

The `users` table will contain:
- `id`: integer primary key
- `username`: unique string
- `password_hash`: string
- `created_at`: datetime

## UV Workflow
The implementation will document and verify this workflow:

- `uv python pin 3.12` or equivalent `.python-version` creation.
- `uv sync --dev` to create `.venv` and install all dependencies.
- `uv run uvicorn app.main:app --reload` to run the local server.
- `uv run pytest` to run automated tests.

## Error Handling
Duplicate usernames will return a visible registration error. Invalid login attempts will return a generic login error. Anonymous access to the protected, change-password, and add-user pages will require login. Password changes with an incorrect current password will preserve the existing password hash and show a readable error. Unknown users in path parameter examples will return a readable not-found page or a 404 response. Database setup errors should fail loudly during development rather than silently hiding configuration problems.

## Testing Strategy
Tests will cover route availability, GET/POST comparison behavior, GET query handling, path parameter lookup, POST form parsing, in-page explanation content, database concept page behavior, user registration, password hashing, successful login, failed login, protected page redirects, logged-in protected page access, password change success/failure, authenticated user creation, anonymous user-creation rejection, the commercial stack explanation page, and the final summary page. Tests should use a temporary SQLite database so local development data and test data remain separate.

## Decision Log
| Decision | Options Considered | Chosen | Reason |
|----------|--------------------|--------|--------|
| Web style | Server-rendered HTML, API-only backend, frontend SPA | Server-rendered HTML | Best fit for teaching forms, GET/POST, and browser-to-backend flow with minimal tooling. |
| Database | SQLite, PostgreSQL, in-memory only | SQLite | Requires no separate database service and makes table creation visible for beginners. |
| Database access | Raw `sqlite3`, SQLAlchemy | Raw `sqlite3` | Better for a short beginner lesson because SQL statements and rows remain visible. |
| Login state | Teaching cookie, Starlette session middleware, JWT | Teaching cookie | Lowest moving parts for showing the login concept; documentation must say this is not production auth. |
| Password handling | Plaintext, third-party hasher, standard-library PBKDF2 | Standard-library PBKDF2 | Avoids plaintext while reducing dependency count for beginners. |
| Environment management | `venv` plus `pip`, Poetry, uv | `uv` | Gives one repeatable workflow for virtual environment creation, dependency sync, command execution, and lockfile management. |
