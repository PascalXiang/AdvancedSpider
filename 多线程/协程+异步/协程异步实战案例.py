# 每天一遍自律读书
import asyncio
import time

import requests
from lxml import etree
import aiohttp
import aiofiles

"""
笔趣阁完美世界爬取
"""


def get_page_info(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    while 1:
        try:
            res = requests.get(url, headers=headers, verify=False)
            res.encoding = "utf-8"
            tree = etree.HTML(res.text)
            total_list = {"title": "content"}
            title = tree.xpath("//div[@id='content_read']/div/div[2]/h1/text()")
            content = tree.xpath("//*[@id='content']//p/text()")
            for t in title:
                t = t.split(" ")
                print(t)
        except:
            print("重来一次")
            time.sleep(1)


def main():
    # 1.拿到页面章节中的每一个url
    # for i in range(1,2):
    url = "https://172.67.137.67/16750/223331.html"
    # 2.启动协程开始异步下载
    get_page_info(url)


if __name__ == '__main__':
    main()
