# 每天一遍自律读书
import requests
import lxml

url = "https://www.pearvideo.com/video_1770138"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Referer": "https://www.pearvideo.com/video_1770138"
}

# 防盗链 -> 当前请求的上一级是谁
contId = url.split("_")[1]
videoStatus = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.5277973110007577"
res = requests.get(videoStatus, headers=headers)
dic = res.json()
srcUrl = dic['videoInfo']['videos']['srcUrl']
systemTime = dic['systemTime']
srcUrl = srcUrl.replace(systemTime, f"cont-{contId}")

# 下载视频
with open("a.mp4", "wb") as f:
    f.write(requests.get(srcUrl, headers=headers).content)
