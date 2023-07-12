import re
import requests
from bs4 import BeautifulSoup

url = "http://www.xinfadi.com.cn/priceDetail.html"
res = requests.get(url).text

# 初始化bs4对象
page = BeautifulSoup(res,"html.parser")
# print(res)
table = page.find("tbody",attrs={"id":"tableBody"})
trs = table.find_all("tr")
for tr in trs:
    tr = tr.find_all("td")
    print(tr)
print(table)
print(trs)