from fastapi import FastAPI
from test import test_func

app = FastAPI()


@app.get("/")
def main():
    return {
        "message": "Hello my this is"
    }


@app.get("/test")
def main():
    return {
        "message": test_func()
    }
