import time
import asyncio

def sleep(seconds: float):
    start_time = time.time()
    while time.time() < start_time + seconds: # CPU занят всё это время
        pass


async def laundry(volume_of_clothes: int = 1):
    print("Laundry started")
    await asyncio.sleep(volume_of_clothes)
    # await - запускается корутину и ждёт пока она не выполнится
    print("Laundry finished!")


async def cake(salt: bool = True):
    print("Cake started")
    await asyncio.sleep(1)
    print("Cake finished")


async def get_delivery(is_mac: bool = True):
    print("Delivery ordered")
    await asyncio.sleep(1)
    print("Delivery received!")


async def main():
    start = time.time()  # 125
    tasks = [laundry(1), cake(salt=True), get_delivery(is_mac=True)]
    
    await asyncio.gather(*tasks)

    finish = time.time()  # 128
    print("Time taken: %.3f" % (finish - start))


if __name__ == "__main__":
    asyncio.run(main())
