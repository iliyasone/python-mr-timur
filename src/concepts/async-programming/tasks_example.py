import asyncio


async def test_await():
    print("Before sleep")
    await asyncio.sleep(10)
    print("After sleep")


