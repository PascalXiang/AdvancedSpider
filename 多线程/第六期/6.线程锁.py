import threading

lock = threading.Lock()

lock.acquire()  # 上锁
lock.release()  # 解锁

# 简写
with lock:
    for i in range(5):
        print("hello")  # 自动释放

