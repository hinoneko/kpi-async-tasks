# Task 1

## Description:

Contains code for an asynchronous mapping function async_map, showcasing the use of a callback function.

## Сode part:

```python
import asyncio
from random import random


async def async_map(lst, func, callback):
    error = None
    results = None
    try:
        tasks = [asyncio.create_task(func(x)) for x in lst]
        results = await asyncio.gather(*tasks, return_exceptions=True)
    except Exception as e:
        error = str(e)

    return callback(results, error)


async def multiply_by_two(x):
    try:
        delay = random()
        await asyncio.sleep(delay)
        return x * 2
    except Exception as e:
        raise RuntimeError(f"Error in multiply_by_two({x}): {e}")


def print_results(results, error):
    if error is not None:
        print(f"Callback received an error: {error}")
    else:
        for res in results:
            if isinstance(res, Exception):
                print(f"Error in task: {res}")
            else:
                print(f"Result: {res}")

    return results


async def main():
    nums_lst = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    for sublist in nums_lst:
        print(f"Processing sublist: {sublist}")
        results = await async_map(sublist, multiply_by_two, print_results)
        print("---")

asyncio.run(main())
```
