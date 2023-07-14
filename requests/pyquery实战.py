from pyquery import PyQuery
import requests
from pyquery import PyQuery
# url = "https://www.baidu.com/"
# headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
# }
#
# res = requests.get(url,headers=headers)
# res.encoding = "utf-8"
# res = res.text
# page = PyQuery(res)
# it = page("li a").items()
# for i in it:
#     href = i.attr("href")
#     text = i.text()
#     print(text,href)

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}


def get_page_source(url):
    res = requests.get(url, headers=headers)
    res.encoding = "gbk"
    return res.text


def parse_page_source(html):
    doc = PyQuery(html)
    pass


def main():
    url = "https://k.autohome.com.cn/146#pvareaid=3454440"
    html = get_page_source(url)
    parse_page_source(html)


if __name__ == '__main__':
    main()
