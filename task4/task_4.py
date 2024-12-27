import asyncio
from random import random


class AsyncRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    async def __aiter__(self):
        for i in range(self.start, self.end):
            delay = random()
            await asyncio.sleep(delay)
            yield i


def async_iterator_demo():
    async def consume_generator():
        async for number in AsyncRange(5):
            print(f"Generated number: {number}")

    return consume_generator

async def main():
    await asyncio.create_task(async_iterator_demo()())

asyncio.run(main())