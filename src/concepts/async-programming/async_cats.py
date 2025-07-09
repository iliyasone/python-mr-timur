import asyncio
import aiohttp

# API_KEY=""



url = "https://cdn2.thecatapi.com/images/ach.jpg"

async def main():
    client = aiohttp.ClientSession()

    async with client.get(url) as response:
        content = await response.read()
        with open("ach.jpg", "wb") as f: 
            f.write(content)

    await client.close()


if __name__ == '__main__':
    asyncio.run(main())


def example_context_manager():
    # file = open()
    with open() as file:
        # file.__enter__
        ...

        # file.__exit__

async def example_async_context_manager():
    async with aopen() as file: 
        # await file.__aenter__()
        ...
        # await file.__aexit()