from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def main():
    return {
        "message": "Hello my this is"
    }
