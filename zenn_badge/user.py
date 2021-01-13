from pydantic import BaseModel


class User(BaseModel):
    username: str
    total_liked_count: int
    articles_count: int
    books_count: int
    scraps_count: int
    follower_count: int
    following_count: int
