# 每天一遍自律读书
import asyncio
import requests
from lxml import etree
import os
from concurrent.futures import ThreadPoolExecutor


# 1.拿到主页面源代码(不需要异步)
# 2.拿到页面源代码后，需要解析出<卷名>,<章节，href>
# 3.

def get_cha_info(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
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
                'chapter_name':chapter_name,
                'url': real_href
            }
            total_list.append(dic)
    return total_list
    # 获取到文章标题与文章内容了


async def download(result):
    for r in result:
        title = result['title']
        url = result['url']  # 用来下载
    pass


def main():
    url = 'https://www.mingchaonaxieshi.com'
    result = get_cha_info(url)
    print(result)
    # 开始上协程
    # asyncio.run(download(result))


if __name__ == '__main__':
    main()
