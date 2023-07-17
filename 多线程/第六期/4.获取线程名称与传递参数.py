import threading
import time


def func(name):
    time.sleep(3)
    print(f"{name}李圣杰")


if __name__ == '__main__':
    thread_list = []
    t = time.time()
    for i in range(10):
        the = threading.Thread(target=func,args=("林允儿",),name='Pascal')
        the.start()
        thread_list.append(the)
    for thread in thread_list:
        thread.join()
    print(time.time() - t)