# 每天一遍自律读书
import requests
import asyncio
import aiohttp
import aiofiles

async def download(url):
    print("开始下载:" + url)
    file_name = url.split("/")[-1]
    # 相当于requests
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            content = await res.content.read()
            # 写入文件
            async with aiofiles.open(file_name, mode="wb") as f:
                await f.write(content)
    print("下载完成:" + url)

async def main():
    url_list = [
        "https://www.win3000.com/pic/10532.html",
        "https://www.win3000.com/pic/10530.html",
        "https://www.win3000.com/pic/10530_4.html"
    ]
    tasks = []
    for url in url_list:
        task = asyncio.create_task(download(url))
        tasks.append(task)
    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())