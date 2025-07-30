import asyncio
from typing import Any
import aiohttp

# API_KEY=""


url = "https://cdn2.thecatapi.com/images/ach.jpg"

json_url = "https://api.thecatapi.com/v1/images/search?limit=100&api_key="


async def get_cats_url(client: aiohttp.ClientSession):
    response = await client.get(json_url)
    response.raise_for_status()
    return await response.json()


async def get_cat_by_url(
    client: aiohttp.ClientSession,
    url: str,
):
    """Download cat pic by url to the cats folder."""
    response: aiohttp.ClientResponse = await client.get(url)
    response.raise_for_status()
    content = await response.read()
    picture_path = "cats/cat_pic.jpg" # TODO: сделать правильное имя
    with open(picture_path, "wb") as f:
        f.write(content)


async def main():
    client = aiohttp.ClientSession()
    await get_cat_by_url(client, url)
    await client.close()


