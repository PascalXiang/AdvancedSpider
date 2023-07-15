# 每天一遍自律读书
import asyncio


async def func1():
    print("1")
    await asyncio.sleep(1)
    print("1结束")
    return "1的返回值"


async def func2():
    print("2")
    await asyncio.sleep(2)
    print("2结束")
    return "2的返回值"


async def func3():
    print("3")
    await asyncio.sleep(3)
    print("3结束")
    return "3的返回值"

async def main():
    f1 = func1()
    f2 = func2()
    f3 = func3()
    tasks = [
        asyncio.create_task(f1),
        asyncio.create_task(f2),
        asyncio.create_task(f3)
    ]
    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())