from concurrent.futures import ThreadPoolExecutor
import time


def func(name, t):
    time.sleep(t)
    print("我是" + name)
    return name


def fn(res):
    print(res.result())


if __name__ == '__main__':
    with ThreadPoolExecutor(3) as t:
        # t.submit(func, "李圣杰", 2).add_done_callback(fn)
        # t.submit(func, "王力宏", 1).add_done_callback(fn)
        # t.submit(func, "周杰伦", 3).add_done_callback(fn)

        # 返回callback执行的顺序是不确定的，返回值的顺序是不确定的
        result = t.map(func, ["李圣杰", "王力宏", "周杰伦"], [2, 1, 3])  # result这里是一个生成器
        for r in result:
            print(r)

        # map的返回值是生成器，返回的内容和任务分发的顺序是一致的
