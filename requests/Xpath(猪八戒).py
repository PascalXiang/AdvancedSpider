from lxml import etree
import requests

url = "https://www.zbj.com/search/service/?kw=sass&r=2"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
response.encoding = "utf-8"
tree = etree.HTML(response.text)
divs = tree.xpath("//div[@class='search-result-list-service']//div")
price = []
name = []
for div in divs:
    name = div.xpath("//div[@class='shop-info text-overflow-line']/text()")
    price = div.xpath("//div[@class='bot-content']/div[1]/span/text()")
    name = "".join(name)
print(name)
