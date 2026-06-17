import os
from pathlib import Path
import sqlite3

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app import database
from app.auth import hash_password, verify_password, get_current_user, require_login

BASE_DIR = Path(__file__).parent

app = FastAPI(title="FastAPI Teaching Site")

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

# Initialise database on startup
database.init_db()


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html")


# ---------------------------------------------------------------------------
# GET vs POST comparison
# ---------------------------------------------------------------------------

@app.get("/methods", response_class=HTMLResponse)
async def methods(request: Request):
    return templates.TemplateResponse(request, "methods.html")


@app.get("/methods/get-demo", response_class=HTMLResponse)
async def methods_get_demo(request: Request, message: str = ""):
    return templates.TemplateResponse(request, "methods_get_result.html", {"message": message})


@app.post("/methods/post-demo", response_class=HTMLResponse)
async def methods_post_demo(request: Request, message: str = Form("")):
    return templates.TemplateResponse(request, "methods_post_result.html", {"message": message})


# ---------------------------------------------------------------------------
# Search — query parameter demo
# ---------------------------------------------------------------------------

@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, q: str = ""):
    return templates.TemplateResponse(request, "search.html", {"q": q})


# ---------------------------------------------------------------------------
# Form demo
# ---------------------------------------------------------------------------

@app.get("/form", response_class=HTMLResponse)
async def form_page(request: Request):
    return templates.TemplateResponse(request, "form.html")


@app.post("/form", response_class=HTMLResponse)
async def form_submit(
    request: Request,
    name: str = Form(""),
    message: str = Form(""),
):
    return templates.TemplateResponse(request, "form_result.html", {"name": name, "message": message})


# ---------------------------------------------------------------------------
# Commercial stack explanation
# ---------------------------------------------------------------------------

@app.get("/commercial-stack", response_class=HTMLResponse)
async def commercial_stack(request: Request):
    return templates.TemplateResponse(request, "commercial_stack.html")


# ---------------------------------------------------------------------------
# Database concept page and user lookup
# ---------------------------------------------------------------------------

@app.get("/database", response_class=HTMLResponse)
async def database_page(request: Request):
    return templates.TemplateResponse(request, "database.html")


@app.get("/users/{user_id}", response_class=HTMLResponse)
async def user_detail(request: Request, user_id: int):
    user = database.get_user_by_id(user_id)
    return templates.TemplateResponse(request, "user_detail.html", {"user": user, "user_id": user_id})


# ---------------------------------------------------------------------------
# Registration
# ---------------------------------------------------------------------------

@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse(request, "register.html", {"error": None})


@app.post("/register")
async def register_submit(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
):
    existing = database.get_user_by_username(username)
    if existing:
        return templates.TemplateResponse(
            request,
            "register.html",
            {"error": f"Username '{username}' already exists. Please choose another."},
        )
    hashed = hash_password(password)
    database.create_user(username, hashed)
    return RedirectResponse("/login?registered=1", status_code=303)


# ---------------------------------------------------------------------------
# Login / logout (full implementation in Task 5)
# ---------------------------------------------------------------------------

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request, registered: str = ""):
    return templates.TemplateResponse(
        request, "login.html", {"error": None, "registered": registered == "1"}
    )


@app.post("/login")
async def login_submit(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
):
    user = database.get_user_by_username(username)
    if user and verify_password(password, user["password_hash"]):
        response = RedirectResponse("/protected", status_code=303)
        response.set_cookie("teaching_user", username, httponly=True)
        return response
    return templates.TemplateResponse(
        request, "login.html", {"error": "Invalid username or password.", "registered": False}
    )


@app.post("/logout")
async def logout(request: Request):
    response = RedirectResponse("/login", status_code=303)
    response.delete_cookie("teaching_user")
    return response


@app.get("/protected", response_class=HTMLResponse)
async def protected(request: Request):
    username = get_current_user(request)
    if not username:
        return RedirectResponse("/login", status_code=303)
    return templates.TemplateResponse(request, "protected.html", {"username": username})


# ---------------------------------------------------------------------------
# Password change
# ---------------------------------------------------------------------------

@app.get("/change-password", response_class=HTMLResponse)
async def change_password_page(request: Request):
    if not get_current_user(request):
        return RedirectResponse("/login", status_code=303)
    return templates.TemplateResponse(request, "change_password.html", {"error": None, "success": False})


@app.post("/change-password", response_class=HTMLResponse)
async def change_password_submit(
    request: Request,
    current_password: str = Form(...),
    new_password: str = Form(...),
):
    username = get_current_user(request)
    if not username:
        return RedirectResponse("/login", status_code=303)
    user = database.get_user_by_username(username)
    if not user or not verify_password(current_password, user["password_hash"]):
        return templates.TemplateResponse(
            request, "change_password.html",
            {"error": "Incorrect current password.", "success": False}
        )
    database.update_password(username, hash_password(new_password))
    return templates.TemplateResponse(request, "change_password.html", {"error": None, "success": True})


# ---------------------------------------------------------------------------
# Authenticated user creation
# ---------------------------------------------------------------------------

@app.get("/add-user", response_class=HTMLResponse)
async def add_user_page(request: Request):
    if not get_current_user(request):
        return RedirectResponse("/login", status_code=303)
    return templates.TemplateResponse(request, "add_user.html", {"error": None, "success": False, "created_username": None})


@app.post("/add-user", response_class=HTMLResponse)
async def add_user_submit(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
):
    if not get_current_user(request):
        return RedirectResponse("/login", status_code=303)
    existing = database.get_user_by_username(username)
    if existing:
        return templates.TemplateResponse(
            request, "add_user.html",
            {"error": f"Username '{username}' already exists.", "success": False, "created_username": None}
        )
    database.create_user(username, hash_password(password))
    return templates.TemplateResponse(
        request, "add_user.html",
        {"error": None, "success": True, "created_username": username}
    )


# ---------------------------------------------------------------------------
# Lesson summary
# ---------------------------------------------------------------------------

@app.get("/summary", response_class=HTMLResponse)
async def summary(request: Request):
    return templates.TemplateResponse(request, "summary.html")

