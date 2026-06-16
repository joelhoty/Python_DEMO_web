# Python Demo Web

A simple demo website for beginners, built with **FastAPI** and **Jinja2** templates.

## Features

- Home page with a welcome message
- About page describing the tech stack and getting-started steps
- Responsive CSS styling (no external frameworks needed)

## Tech stack

| Tool | Purpose |
|------|---------|
| [FastAPI](https://fastapi.tiangolo.com) | Web framework |
| [Jinja2](https://jinja.palletsprojects.com) | HTML templating |
| [Uvicorn](https://www.uvicorn.org) | ASGI server |

## Getting started

```bash
# 1. Clone the repo
git clone https://github.com/joelhoty/Python_DEMO_web.git
cd Python_DEMO_web

# 2. Install dependencies (Python 3.11+ required)
pip install -e ".[dev]"

# 3. Start the development server
uvicorn app.main:app --reload

# 4. Open http://localhost:8000 in your browser
```

## Running tests

```bash
pytest
```

## Project layout

```
Python_DEMO_web/
├── app/
│   ├── main.py          # FastAPI application & routes
│   ├── static/
│   │   └── style.css    # Site-wide CSS
│   └── templates/
│       ├── base.html    # Shared layout (nav + footer)
│       ├── index.html   # Home page
│       └── about.html   # About page
├── tests/
│   └── test_main.py     # Pytest tests
└── pyproject.toml       # Project metadata & dependencies
```
