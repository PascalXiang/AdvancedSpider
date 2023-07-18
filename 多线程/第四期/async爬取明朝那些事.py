# 每天一遍自律读书
import asyncio
import aiofiles
import aiohttp
import requests
from lxml import etree
import os


# 1.拿到主页面源代码(不需要异步)
# 2.拿到页面源代码后，需要解析出<卷名>,<章节，href>
# 3.

def get_cha_info(url):
    res = requests.get(url, headers=headers).text
    # 开始解析
    tree = etree.HTML(res)
    book_list = []
    total_list = []
    menu_list = []  # 存储章节标题与章节内容
    for i in range(6, 20, 2):
        book_list.append(tree.xpath(f"//div[@class='page-content']/h2[{i}]/text()")[0])  # 获取所有书卷名称
    for j in range(0, 7):
        ul_list = tree.xpath(f"//div[@class='page-content']/ul[{j}]//li")
        for li in ul_list:
            chapter_name = li.xpath("./a/text()")[0].split()[-1]
            book_name = li.xpath("./a/text()")[0].split()[0]
            href = li.xpath("./a/@href")[0]
            real_href = url + href
            dic = {
                'book_name': book_name,
                'chapter_name': chapter_name,
                'url': real_href
            }
            total_list.append(dic)
    return total_list
    # 获取到文章标题与文章内容了


async def download_one(url, file_path):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as res:
            page_source = await res.text()
            tree = etree.HTML(page_source)
            content = "".join(tree.xpath("//div[@class='single-box clearfix entry-content']//p/text()")).strip()
            async with aiofiles.open(file_path, mode="w", encoding='utf-8') as f:
                await f.write(content)
    print("下载成功!" + file_path)


async def download(result):
    tasks = []
    for r in result:
        book_name = r['book_name']
        title = r['chapter_name']
        url = r['url']  # 用来下载文章内容
        if not os.path.exists(book_name):
            os.makedirs(book_name)  # 如果不在就创建
        # 给出文件的真正保存路径
        file_path = f"{book_name}/{title}.txt"
        t = asyncio.create_task(download_one(url, file_path))
        tasks.append(t)
    await asyncio.wait(tasks)


def main():
    url = 'https://www.mingchaonaxieshi.com'
    result = get_cha_info(url)
    print(result)
    # 开始上协程
    asyncio.run(download(result))


if __name__ == '__main__':
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    main()
