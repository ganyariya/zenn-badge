import requests
from .user import User


def scrape_user(username: str) -> User:
    user_api_url: str = f'https://api.zenn.dev/users/{username}'
    response = requests.get(user_api_url)
    json_data = response.json()['user']
    user = User(**json_data)
    return user
