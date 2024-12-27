import asyncio


async def long_running_task():
    try:
        print("Task started")
        await asyncio.sleep(5)
        print("Task finished")
    except asyncio.CancelledError:
        print("Task was cancelled")

def demonstrate_cancellation():
    async def run_demo():
        task = asyncio.create_task(long_running_task())
        await asyncio.sleep(1)
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            print("Handled cancellation")

    return run_demo

async def main():
    await demonstrate_cancellation()()

asyncio.run(main())