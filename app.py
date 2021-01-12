from fastapi import FastAPI
import datetime

app = FastAPI()


@app.get("/")
def main():
    return {
        "message": "Hello my friend"
    }
