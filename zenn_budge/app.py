from fastapi import FastAPI
from .zenn import scrape_user

app = FastAPI()


@app.get("/")
def main():
    return {
        "message": "Hello my friend"
    }


@app.get("/test")
def test_get():
    scrape_user("ganariya")
    return 0
