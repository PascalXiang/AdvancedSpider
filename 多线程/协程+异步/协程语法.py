# 每天一遍自律读书

import asyncio
async def func():
    print("我是函数")


if __name__ == '__main__':
    # 协程对象想要执行必须借助于event_loop
    f = func()
    # 拿到事件循环
    event_loop = asyncio.get_event_loop()
    # event_loop执行协程对象，直到该对象内的内容执行完毕为止
    # event_loop.run_until_complete(f)
    asyncio.run(f)  # asyncio可以直接执行一个协程对象