import requests

# API_KEY=""
from typing import TypedDict


class CatPicture(TypedDict, total=True):
    id: str
    url: str
    """Url with a cat."""
    width: int
    height: int


json_url = "https://api.thecatapi.com/v1/images/search?limit=10"
url = "https://cdn2.thecatapi.com/images/"


def get_cats_json() -> list[CatPicture]:
    response = requests.get(json_url)
    response.raise_for_status()
    with open("response.json", mode="w") as f:
        f.write(response.text)
    return response.json()


def json_analyzer_300(obj: list[dict]):
    result: list[str] = []
    for i in obj:
        i["url"]


def get_picture(url: str):
    response = requests.get(url)
    response.raise_for_status()
    with open("MTc5NDIyMQ.jpg", "wb") as file:
        file.write(response.content)


# eval('''exec("""import os;print(os.getenv("HELLO", "gs"))""")''')
