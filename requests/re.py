import requests
import re
# 1.拿到页面源代码
# 2.编写正则，提取页面数据
# 3.保存数据

url = "https://movie.douban.com/top250"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}
res = requests.get(url, headers=headers).text
# print(res)
# 编写正则表达式
# re.S可以让正则中的.匹配换行符
obj = re.compile(r'<div class="item">.*?<span class="title">(?P<name>.*?)</span>',re.S)
result = obj.finditer(res)
for item in result:
    print(item.group("name"))