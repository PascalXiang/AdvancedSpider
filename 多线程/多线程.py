from threading import Thread

"""
手动创建线程
"""


def func(name):
    for i in range(10):
        print(name, i)


if __name__ == '__main__':
    s1 = Thread(target=func, args=("周杰伦",))
    s2 = Thread(target=func, args=("王力宏",))
    s1.start()
    s2.start()
