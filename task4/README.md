# Task 4

## Description:

Demonstrates a custom asynchronous iterator (AsyncRange).

## Сode part:

```python
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


async def async_print_range(start, end, string):
    async for number in AsyncRange(start, end):
        print(f"{string}: {number}")


async def main():
    cors = [
        async_print_range(0, 3, "Range 1"),
        async_print_range(3, 6, "Range 2"),
        async_print_range(6, 9, "Range 3"),
    ]
    await asyncio.gather(*cors)

asyncio.run(main())
```
