import asyncio
import time


async def func1():
    print("hello")
    await asyncio.sleep(2)
    print("1结束")


async def func2():
    print("hello")
    await asyncio.sleep(3)
    print("2结束")


async def func3():
    print("hello")
    await asyncio.sleep(1)
    print("3结束")


async def main():
    tasks = [func1(), func2(), func3()]
    task = asyncio.create_task(tasks)
    await asyncio.wait(task)


if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time()
    print(t2 - t1)
