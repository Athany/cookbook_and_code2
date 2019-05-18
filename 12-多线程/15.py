import threading
import time

lock_1 = threading.Lock()
lock_2 = threading.Lock()


def func_1():
    print("func_1 starting.........", time.ctime())
    lock_1.acquire(timeout=9)
    print("func_1 申请了 lock_1....", time.ctime())
    time.sleep(3)
    print("func_1 等待 lock_2.......", time.ctime())

    rst = lock_2.acquire(timeout=5)         # 在func_1函数中社设定了锁2的申请超时时间为5秒，也就是5秒内函数1没有申请到锁2就不再继续申请。
    if rst:
        print("func_1 已经得到锁 lock_2", time.ctime())
        lock_2.release()
        print("func_1 释放了锁 lock_2", time.ctime())
    else:
        print("func_1 注定没申请到lock_2.....", time.ctime())

    lock_1.release()
    print("func_1 释放了 lock_1", time.ctime())
    print("func_1 done..........", time.ctime())


def func_2():
    print("func_2 starting.........", time.ctime())
    lock_2.acquire()
    print("func_2 申请了 lock_2....", time.ctime())
    time.sleep(4)
    print("func_2 等待 lock_1.......", time.ctime())
    lock_1.acquire()
    print("func_2 申请了 lock_1.......", time.ctime())

    lock_1.release()
    print("func_2 释放了 lock_1", time.ctime())

    lock_2.release()
    print("func_2 释放了 lock_2", time.ctime())
    print("func_2 done..........", time.ctime())


if __name__ == "__main__":

    print("主程序启动..............", time.ctime())
    t1 = threading.Thread(target=func_1, args=())
    t2 = threading.Thread(target=func_2, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("主程序结束..............", time.ctime())
