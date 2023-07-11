# 每天一遍自律读书
import requests
import re

"""
1.提取到主页面中每一个电影的背后的那个url地址
    1.拿到“2021必看热片”那一块的html代码
    2.从刚拿到的html代码中提取到href的值
    
2.访问子页面，提取到电影的名称以及下载地址
    1.拿到子页面的页面源代码
    2.数据提取
    3.写入文件
"""

url = "https://www.dy2018.com/"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}
res = requests.get(url,headers).text
res.encode("gbk")
# print(res)

# 1.提取2021必看热片部分的html代码
obj = re.compile(r"2021必看热片.*?<ul>(?P<html>.*?)</ul>",re.S)
result = obj.search(res)
html = result.group("html")
print(html)

# 2.提取a标签中的href的值
obj1 = re.compile(r"<li><a href='(?P<href>.*?)' title")
result1 = obj1.finditer(html)

obj2 = re.compile(r'<div id="Zoom">.*?')
for item in result1:
    # print(item.group("html"))
    # 拼接出子页面的url
    child_url = url.strip("/") + item.group("html")
    child_res = requests.get(url=child_url)
    child_res.encoding = "gbk"

