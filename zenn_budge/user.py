from pydantic import BaseModel


class User(BaseModel):
    username: str
    total_liked_count: int
    articles_count: int
    follower_count: int
