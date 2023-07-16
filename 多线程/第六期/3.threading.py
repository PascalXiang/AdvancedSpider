# 每天一遍自律读书
import threading
import time

import aiohttp


def run():
    print("线程开始")
    time.sleep(1)
    print("线程结束")

if __name__ == '__main__':
    thread_list = []
    t = time.time()
    for i in range(5):
        thread = threading.Thread(target=run)
        thread.start()
        thread_list.append(thread)
    for thr in thread_list:
        thr.join()
    print(time.time() - t)
