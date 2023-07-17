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
    task_list = [asyncio.create_task(func1()), asyncio.create_task(func2()), asyncio.create_task(func3())]
    await asyncio.wait(task_list)


if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time()
    print(t2 - t1)
