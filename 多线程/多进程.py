# 每天一遍自律读书
from multiprocessing import Process,Queue
import requests

# 队列：可以进行进程之间的通信
def func(name,queue):
    for i in range(1000):
        print(name,i)

if __name__ == '__main__':
    q = Queue()
    s1 = Process(target=func,args=("李圣杰",q))
    s2 = Process(target=func,args=("周杰伦",q))
    s1.start()
    s2.start()

    # 多线程：一般用于任务相对统一
    # 多进程：一般用于任务相对独立