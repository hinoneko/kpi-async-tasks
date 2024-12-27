# Task 2

## Description:

Contains an asynchronous async_map function that returns results directly (no callback).

## Сode part:

```python
import asyncio
from random import random


async def async_map(lst, func):
    tasks = [asyncio.create_task(func(item)) for item in lst]
    results = await asyncio.gather(*tasks)

    return results


async def multiply_by_two(x):
    delay = random()
    await asyncio.sleep(delay)

    return x * 2


async def main():
    nums_lst = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    cors = [async_map(nums, multiply_by_two) for nums in nums_lst]
    tasks = asyncio.gather(*cors)
    results = await tasks
    print(f"Results: {results}")

asyncio.run(main())
```
