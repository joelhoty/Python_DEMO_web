# Delta for Teaching Site

## ADDED Requirements

### Requirement: UV Managed Python Environment
The system MUST define a repeatable Python environment managed by `uv`.

#### Scenario: Install project dependencies
- GIVEN `uv` is installed on the developer machine
- WHEN the developer runs `uv sync --dev`
- THEN project runtime and development dependencies SHALL be installed into the local `.venv`

#### Scenario: Run server through uv
- GIVEN dependencies are installed
- WHEN the developer runs `uv run uvicorn app.main:app --reload`
- THEN the FastAPI development server SHALL start using the project environment

### Requirement: Runnable FastAPI Website
The system MUST provide a runnable FastAPI website with HTML pages rendered from templates.

#### Scenario: Start the teaching site
- GIVEN project dependencies are installed
- WHEN the developer starts the FastAPI application
- THEN the site SHALL serve an HTML home page from `GET /`

### Requirement: GET Variable Passing Examples
The system MUST demonstrate GET-based variable passing through both query parameters and path parameters.

#### Scenario: Query parameter example
- GIVEN the site is running
- WHEN a user visits `/search?q=fastapi`
- THEN the response SHALL display the submitted query value

#### Scenario: Path parameter example
- GIVEN a user exists with id `1`
- WHEN a user visits `/users/1`
- THEN the response SHALL display details for that user or a clear not-found message

### Requirement: Interactive GET And POST Comparison
The system MUST provide a teaching page that lets learners operate GET and POST examples and compare their differences.

#### Scenario: Operate GET example
- GIVEN the learner is on the GET and POST comparison page
- WHEN the learner submits a value through the GET example
- THEN the browser SHALL show the value in the URL query string and the page SHALL explain that GET sends variables through the URL

#### Scenario: Operate POST example
- GIVEN the learner is on the GET and POST comparison page
- WHEN the learner submits a value through the POST example
- THEN the browser SHALL not show the submitted value in the URL query string and the page SHALL explain that POST sends variables in the request body

#### Scenario: Compare GET and POST result
- GIVEN the learner has submitted examples through both methods
- WHEN the result renders
- THEN the page SHALL show a concise comparison of where the variable was sent, what the backend received, and when each method is commonly used

### Requirement: POST Form Submission Examples
The system MUST demonstrate POST-based form submission using standard HTML forms.

#### Scenario: Submit a basic form
- GIVEN the user is on a form example page
- WHEN the user submits form fields by POST
- THEN the server SHALL read the form values and render a response containing the submitted values

### Requirement: Interactive Concept Page Pattern
The system MUST present core concepts using a consistent explanation-plus-operation pattern.

#### Scenario: Use a form concept page
- GIVEN the learner is on the form concept page
- WHEN the learner reads the page and submits the form
- THEN the page SHALL show the concept explanation, the submitted values, and a short explanation of how FastAPI received the form variables

#### Scenario: Use a database concept page
- GIVEN the learner is on the database concept page
- WHEN the learner creates or looks up a user
- THEN the page SHALL show the concept explanation, the database action that occurred, and the resulting user data or error message

### Requirement: In-Page Function Explanations
The system MUST let learners use the demo website while reading concise explanations of the current page's backend concept.

#### Scenario: View route explanation while using a page
- GIVEN the learner is viewing a teaching page
- WHEN the page renders
- THEN the page SHALL show the relevant route, HTTP method, data source, and backend action in beginner-friendly language

#### Scenario: View database explanation after an action
- GIVEN the learner submits a registration or login form
- WHEN the response renders
- THEN the page SHALL explain whether the action read from or wrote to the database

### Requirement: SQLite User Database
The system MUST store user records in SQLite through a small database layer built on Python's standard-library `sqlite3` module.

#### Scenario: Create user database
- GIVEN the application starts with no existing database
- WHEN database initialization runs
- THEN the users table SHALL be available with fields for id, username, password hash, and creation timestamp

#### Scenario: Register a new user
- GIVEN no existing user has username `alice`
- WHEN `alice` submits the registration form with a password
- THEN a user record SHALL be created in the database

### Requirement: Secure Password Storage
The system MUST hash user passwords before storage and MUST NOT store plaintext passwords.

#### Scenario: Store password hash
- GIVEN a user registers with password `secret123`
- WHEN the user record is saved
- THEN the database SHALL contain a password hash and SHALL NOT contain `secret123`

### Requirement: Basic Login Flow
The system MUST allow registered users to log in with username and password.

#### Scenario: Successful login
- GIVEN a registered user has a valid password hash
- WHEN the user submits the correct username and password
- THEN the system SHALL mark the browser session as logged in and redirect to a protected page

#### Scenario: Failed login
- GIVEN a registered user exists
- WHEN the user submits an incorrect password
- THEN the system SHALL reject the login and display an error without exposing whether the password hash matched internally

### Requirement: Protected Page
The system MUST include at least one page that requires login.

#### Scenario: Anonymous access to protected page
- GIVEN a browser session is not logged in
- WHEN the user visits the protected page
- THEN the system SHALL redirect the user to the login page or return a clear authentication-required response

#### Scenario: Logged-in access to protected page
- GIVEN a browser session is logged in
- WHEN the user visits the protected page
- THEN the system SHALL display protected content for that user

### Requirement: Authenticated Password Change
The system MUST include a logged-in password change example as part of the core teaching flow.

#### Scenario: Change password successfully
- GIVEN a browser session is logged in
- WHEN the user submits the current password and a new password
- THEN the system SHALL verify the current password, store a hash for the new password, and keep plaintext passwords out of the database

#### Scenario: Reject password change with wrong current password
- GIVEN a browser session is logged in
- WHEN the user submits an incorrect current password
- THEN the system SHALL reject the password change and keep the existing password hash

### Requirement: Authenticated User Creation
The system MUST include a logged-in user creation example as part of the core teaching flow.

#### Scenario: Logged-in user creates another user
- GIVEN a browser session is logged in
- WHEN the user submits a new username and password on the add-user form
- THEN the system SHALL create the new user with a hashed password

#### Scenario: Anonymous user cannot create another user
- GIVEN a browser session is not logged in
- WHEN the user submits or visits the add-user page
- THEN the system SHALL require login before allowing user creation

### Requirement: Commercial Stack Explanation
The system MUST include a short teaching page or section explaining how frontend, backend, database, and server choices commonly fit together in commercial systems.

#### Scenario: View commercial stack explanation
- GIVEN the site is running
- WHEN a learner visits the commercial stack explanation page or section
- THEN the response SHALL describe example technologies for frontend, backend, database, and server hosting without requiring those technologies in the demo

### Requirement: Lesson Summary
The system MUST include a final summary page after the account-management examples.

#### Scenario: View final lesson summary
- GIVEN the learner has reached the end of the demo sequence
- WHEN the learner visits the summary page
- THEN the response SHALL summarize route design, GET/POST variable passing, form handling, database reads/writes, password hashing, login state, password change, and logged-in user creation

### Requirement: Focused Automated Tests
The system MUST include automated tests for core teaching behavior.

#### Scenario: Verify core routes
- GIVEN the test suite is run
- WHEN route, form, database, and authentication tests execute
- THEN the tests SHALL verify successful and failing cases for GET, POST, in-page explanations, registration, login, protected page access, password change, authenticated user creation, and the summary page

## MODIFIED Requirements

No existing requirements are modified because this project currently has no implemented application requirements.

## REMOVED Requirements

No existing requirements are removed.
