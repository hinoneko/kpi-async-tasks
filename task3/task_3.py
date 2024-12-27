import asyncio


async def long_running_task():
    try:
        print("Task started")
        await asyncio.sleep(5)
        print("Task finished")
    except asyncio.CancelledError:
        print("Task was cancelled")
        raise


async def main():
    task = asyncio.create_task(long_running_task())

    await asyncio.sleep(1)
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("Handled cancellation")

asyncio.run(main())