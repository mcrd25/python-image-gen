import asyncio

async def my_function():
    # Async code goes here
    return "Hello, World!"

async def main():
    task = asyncio.create_task(my_function())
    result = await task
    print(result)

asyncio.run(main())
