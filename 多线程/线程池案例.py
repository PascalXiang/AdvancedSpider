import requests
from concurrent.futures import ThreadPoolExecutor
from lxml import etree
import time


f = open("data.scv",mode="w",encoding="utf-8")
def download(url):
    new_url = "http://www.xinfadi.com.cn/getPriceData.html"
    res = requests.post(new_url, headers=headers).text
    res.encode("utf-8")
    tree = etree.HTML(res)
    table_list = tree.xpath("//tbody[@id='tableBody']/tr")
    print(res)
    for tr in table_list:
        s = "".join(tr)
        f.write(s)
        f.write("\n")
        print(tr)


# def getName():
#     print("你的名字")


if __name__ == '__main__':
    url = "http://www.xinfadi.com.cn/priceDetail.html"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    with ThreadPoolExecutor(20) as t:
        for i in range(10):
            t.submit(download,url)
    download(url)


