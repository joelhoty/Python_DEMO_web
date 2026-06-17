# Tasks: Create FastAPI Teaching Site

> **For agentic workers:** Use sos-apply to implement these tasks with subagent-driven development, TDD, and automated code review.

**Goal:** Build a runnable FastAPI teaching website that demonstrates GET, POST, form data, variable passing, SQLite CRUD, registration, login, protected pages, password change, logged-in user creation, and a final summary, with in-page explanations throughout.

**Architecture:** Use server-rendered FastAPI with Jinja2 templates and SQLite persistence through the standard-library `sqlite3` module. Manage the environment with `uv`, declare a small dependency set in `pyproject.toml`, and keep the implementation beginner-readable while still hashing passwords with standard-library tools.

---

### Task 1: Project Skeleton And Dependencies

**Files:**
- Create: `app/__init__.py`
- Create: `app/main.py`
- Create: `pyproject.toml`
- Create: `.python-version`
- Create: `tests/conftest.py`
- Create: `uv.lock`

- [x] **Step 1: Write failing test** for `GET /` returning an HTML response.
- [x] **Step 2: Verify test fails** before the app exists.
- [x] **Step 3: Configure uv project dependencies** with FastAPI, Uvicorn, Jinja2, form parsing, pytest, and httpx.
- [x] **Step 4: Implement minimal FastAPI app** with a home route and required dependencies.
- [x] **Step 5: Verify test passes** with `uv run pytest`.
- [x] **Step 6: Checkpoint** skeleton and dependency setup.

### Task 2: Templates And Teaching Pages

**Files:**
- Create: `app/templates/base.html`
- Create: `app/templates/index.html`
- Create: `app/templates/methods.html`
- Create: `app/templates/form.html`
- Create: `app/templates/form_result.html`
- Create: `app/templates/database.html`
- Create: `app/templates/search.html`
- Create: `app/templates/commercial_stack.html`
- Create: `app/static/styles.css`
- Modify: `app/main.py`
- Test: `tests/test_teaching_routes.py`

- [x] **Step 1: Write failing tests** for GET/POST comparison behavior, query parameter display, POST form result rendering, in-page route/method explanations, and commercial stack explanation content.
- [x] **Step 2: Verify tests fail** against the skeleton.
- [x] **Step 3: Implement templates, explanation panels, static CSS, `GET /methods`, `GET /methods/get-demo`, `POST /methods/post-demo`, `GET /search`, `GET /form`, `POST /form`, and `GET /commercial-stack`.**
- [x] **Step 4: Verify tests pass** for GET and POST teaching examples.
- [x] **Step 5: Checkpoint** teaching pages.

### Task 3: SQLite User Model

**Files:**
- Create: `app/database.py`
- Modify: `app/main.py`
- Test: `tests/test_users.py`

- [x] **Step 1: Write failing tests** for database initialization, user creation, `GET /database`, and `GET /users/{user_id}` lookup.
- [x] **Step 2: Verify tests fail** before the database layer exists.
- [x] **Step 3: Implement standard-library `sqlite3` database setup, users table creation, parameterized insert/select helpers, database concept page, and user lookup route.**
- [x] **Step 4: Verify tests pass** using an isolated test database.
- [x] **Step 5: Checkpoint** database helper and lookup behavior.

### Task 4: Registration And Password Hashing

**Files:**
- Create: `app/auth.py`
- Create: `app/templates/register.html`
- Modify: `app/main.py`
- Test: `tests/test_auth.py`

- [x] **Step 1: Write failing tests** for registration, duplicate username handling, and no plaintext password storage.
- [x] **Step 2: Verify tests fail** before auth helpers exist.
- [x] **Step 3: Implement `hashlib.pbkdf2_hmac` password helpers, salt generation with `secrets`, and registration routes.**
- [x] **Step 4: Verify tests pass** for registration and password storage behavior.
- [x] **Step 5: Checkpoint** registration and password hashing.

### Task 5: Login Session And Protected Page

**Files:**
- Create: `app/templates/login.html`
- Create: `app/templates/protected.html`
- Modify: `app/auth.py`
- Modify: `app/main.py`
- Test: `tests/test_auth.py`

- [x] **Step 1: Write failing tests** for successful login, failed login, logout, anonymous protected access, and logged-in protected access.
- [x] **Step 2: Verify tests fail** before session behavior exists.
- [x] **Step 3: Implement teaching-cookie login/logout routes, current-user helper, and protected page.**
- [x] **Step 4: Verify tests pass** for all authentication flows.
- [x] **Step 5: Checkpoint** login and protected page behavior.

### Task 6: Password Change And Authenticated User Creation

**Files:**
- Create: `app/templates/change_password.html`
- Create: `app/templates/add_user.html`
- Modify: `app/auth.py`
- Modify: `app/main.py`
- Test: `tests/test_auth.py`

- [x] **Step 1: Write failing tests** for password change success, wrong-current-password rejection, authenticated add-user success, and anonymous add-user rejection.
- [x] **Step 2: Verify tests fail** before these routes exist.
- [x] **Step 3: Implement password change routes and authenticated add-user routes with hashed password storage and in-page explanations.**
- [x] **Step 4: Verify tests pass** for password change and authenticated user creation flows.
- [x] **Step 5: Checkpoint** password management and authenticated user creation.

### Task 7: Lesson Summary And Documentation

**Files:**
- Create: `app/templates/summary.html`
- Create: `README.md`
- Modify: `plan.md`
- Modify: `app/main.py`
- Test: `tests/test_teaching_routes.py`

- [x] **Step 1: Write failing test** for final summary page content.
- [x] **Step 2: Verify the summary test fails** before the route exists.
- [x] **Step 3: Implement `GET /summary` with a concise review of GET/POST, forms, database, password hashing, login state, password change, and user creation.**
- [x] **Step 4: Document `uv sync --dev`, `uv run uvicorn app.main:app --reload`, `uv run pytest`, route map, small dependency purpose, teaching-cookie limitation, and teaching sequence.**
- [x] **Step 5: Verify commands, summary content, and route descriptions match the implemented app.**
- [x] **Step 6: Checkpoint** summary and documentation.
