# 每天一遍自律读书
import asyncio


async def func1():
    print("1")
    await asyncio.sleep(1)
    print("1结束")


async def func2():
    print("2")
    await asyncio.sleep(2)
    print("2结束")


async def func3():
    print("3")
    await asyncio.sleep(3)
    print("3结束")


if __name__ == '__main__':
    f1 = func1()
    f2 = func2()
    f3 = func3()
    # 把三个任务放一起
    task = [
        f1,
        f2,
        f3
    ]
    asyncio.run(asyncio.wait(task))
