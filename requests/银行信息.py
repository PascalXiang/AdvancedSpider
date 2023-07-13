import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

workbook = Workbook()
# 选择活动的工作表
worksheet = workbook.active

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

data_list = []  # 创建一个列表，用于存储每次循环迭代的值
j = 0
for i in range(1, 100):
    url = "https://www.chakahao.com/lhh/index_{}.html".format(i)
    res = requests.get(url, headers=headers).text
    page = BeautifulSoup(res, "html.parser")
    name_list = page.find_all("td", attrs={"class": "w-100"})
    num_list = page.find_all("td", attrs={"class": "text-nowrap text-muted"})

    for name, num in zip(name_list, num_list):
        data_list.append({
            "A": name.text,  # 使用列名称，例如 A、B、C
            "B": num.text.strip()
        })
    j = j + 1
    print(j)

# 添加表头
worksheet.append(["Name", "Number"])

# 将数据逐行写入工作表
for row_data in data_list:
    worksheet.append([row_data["A"], row_data["B"]])

# 保存Excel文件
workbook.save("data.xlsx")
print("爬取成功!")
