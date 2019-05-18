import threading
import time

# 参数定义最多几个线程同时使用资源
semaphore = threading.Semaphore(3)


def func():
    if semaphore.acquire():
        for i in range(2):
            print(threading.currentThread().getName() + ' get semaphore', time.ctime())   # 此处只是打印了两次而已
        time.sleep(5)
        semaphore.release()
        print(threading.currentThread().getName() + ' release semaphore', time.ctime())


for j in range(8):
    t1 = threading.Thread(target=func)          # 实例化了8个线程，目标是上面的函数
    t1.start()
