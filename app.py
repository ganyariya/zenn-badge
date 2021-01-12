from fastapi import FastAPI
from test import test

app = FastAPI()


@app.get("/")
def main():
    return {
        "message": "Hello my friend"
    }


@app.get("/test")
def test_get():
    return test()
