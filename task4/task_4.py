import asyncio


class AsyncNumberGenerator:
    def __init__(self, limit):
        self.limit = limit

    async def __aiter__(self):
        for i in range(self.limit):
            await asyncio.sleep(0.1)
            yield i

def async_iterator_demo():
    async def consume_generator():
        async for number in AsyncNumberGenerator(5):
            print(f"Generated number: {number}")

    return consume_generator

async def main():
    await asyncio.create_task(async_iterator_demo()())

asyncio.run(main())