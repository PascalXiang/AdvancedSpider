import requests
res = requests.get("http://www.baidu.com/").text
print(res)