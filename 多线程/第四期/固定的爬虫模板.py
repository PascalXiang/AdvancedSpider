# 每天一遍自律读书
import asyncio
import time

import aiohttp


async def get_page_source(url):
    # 网络请求
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            text = await res.text()
            return print(text)


async def main():
    urls = [
        "https://www.baidu.com/",
        # "https://www.google.com/",
        "https://www.jd.com/"
    ]

    tasks = []

    for url in urls:
        tasks.append(asyncio.create_task(get_page_source(url)))

    # 方案1
    # await asyncio.wait(tasks)

    # 方案2
    result = await asyncio.gather(*tasks)    # 和wait差不多
    for r in result:
        print(r)


if __name__ == '__main__':
    t1 = time.time()
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())
    print(time.time() - t1)
