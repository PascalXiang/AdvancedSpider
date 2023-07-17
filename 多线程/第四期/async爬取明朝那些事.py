# 每天一遍自律读书
import asyncio
import requests
from lxml import etree


# 1.拿到主页面源代码(不需要异步)
# 2.拿到页面源代码后，需要解析出<卷名>,<章节，href>
# 3.

def get_cha_info(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    res = requests.get(url,headers=headers).text
    # 开始解析
    tree = etree.HTML(res)
    total = tree.xpath("//div[@class='page-content']")
    # print(len(total))
    result = []

    return result

def main():
    url = 'https://www.mingchaonaxieshi.com/'
    get_cha_info(url)
    pass



if __name__ == '__main__':
    main()