# Task 1

## Description:

Contains code for an asynchronous mapping function async_map, showcasing the use of a callback function.

## Сode part:

```python
import asyncio
from random import random


async def async_map(lst, func, callback):
    tasks = [asyncio.create_task(func(item)) for item in lst]
    results = await asyncio.gather(*tasks)

    return callback(results)


async def multiply_by_two(x):
    delay = random()
    await asyncio.sleep(delay)

    return x * 2


def print_results(results):
    print(f"Results: {results}")

    return results


async def main():
    nums_lst = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    cors = [async_map(nums, multiply_by_two, print_results) for nums in nums_lst]
    tasks = asyncio.gather(*cors)
    await tasks

asyncio.run(main())
```
