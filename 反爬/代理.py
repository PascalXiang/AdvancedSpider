import requests
url = "https://www.baidu.com/"

proxy = {
    "http":"http://118.190.244.234:3128",
    "https":"https://118.190.244.234:3128"
}
res = requests.get(url,proxies=proxy)
res.encoding = 'utf-8'
print(res.text)
