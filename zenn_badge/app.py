import pybadges

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .zenn import scrape_user
from .user import User
from .badge import make_badge

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
def main() -> str:
    return "Zenn Badges"


# @app.get("/items/{id}", response_class=HTMLResponse)
# def read_item(request: Request, id: str):
#     return templates.TemplateResponse('index.html', {"request": request, "id": id})


@app.get("/{username}/liked", response_class=HTMLResponse)
def get_liked(username: str):
    user: User = scrape_user(username)
    badge = make_badge(username, 'Zenn liked', str(user.total_liked_count))
    return HTMLResponse(content=badge, status_code=200, media_type='image/svg+xml')


@app.get("/{username}/articles", response_class=HTMLResponse)
def get_articles(username: str):
    user: User = scrape_user(username)
    badge = make_badge(username, 'Zenn articles', str(user.articles_count))
    return HTMLResponse(content=badge, status_code=200, media_type='image/svg+xml')


@app.get("/{username}/books", response_class=HTMLResponse)
def get_books(username: str):
    user: User = scrape_user(username)
    badge = make_badge(username, 'Zenn books', str(user.books_count))
    return HTMLResponse(content=badge, status_code=200, media_type='image/svg+xml')


@app.get("/{username}/scraps", response_class=HTMLResponse)
def get_scraps(username: str):
    user: User = scrape_user(username)
    badge = make_badge(username, 'Zenn scraps', str(user.scraps_count))
    return HTMLResponse(content=badge, status_code=200, media_type='image/svg+xml')


@app.get("/{username}/followers", response_class=HTMLResponse)
def get_followers(username: str):
    user: User = scrape_user(username)
    badge = make_badge(username, 'Zenn followers', str(user.follower_count))
    return HTMLResponse(content=badge, status_code=200, media_type='image/svg+xml')


@app.get("/{username}/followings", response_class=HTMLResponse)
def get_followings(username: str):
    user: User = scrape_user(username)
    badge = make_badge(username, 'Zenn followings', str(user.following_count))
    return HTMLResponse(content=badge, status_code=200, media_type='image/svg+xml')
