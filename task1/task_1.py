import asyncio

def async_map(lst, func, callback):
    async def apply_map():
        tasks = [asyncio.create_task(func(item)) for item in lst]
        results = await asyncio.gather(*tasks)
        callback(results)

    return apply_map()

def demo_async_map():
    async def multiply_by_two(x):
        await asyncio.sleep(0.1)
        return x * 2

    def print_results(results):
        print("Task 1 Results:", results)

    numbers = [1, 2, 3, 4]
    await async_map(numbers, multiply_by_two, print_results)

async def main():
    await demo_async_map()

asyncio.run(main())