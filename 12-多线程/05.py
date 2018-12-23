import time
import threading


def loop1(in1):
    # ctime得到当前时间
    print("Start loop 1 at:", time.ctime())
    print("我是参数",in1)
    # 睡眠时间
    time.sleep(4)
    print("End loop 1 at:", time.ctime())


def loop2(in1, in2):
    # ctime得到当前时间
    print("Start loop 2 at:", time.ctime())
    print("我是参数", in1, "和参数", in2)
    # 睡眠时间
    time.sleep(2)
    print("End loop 2 at:", time.ctime())


def main():
    print("Start at:", time.ctime())
    # 启用多线程去执行两个函数
    # 生成threading.Thread实例
    t1 = threading.Thread(target=loop1, args=("aaa",))
    t1.start()
    t2 = threading.Thread(target=loop2, args=("zsj", "zx",))
    t2.start()
    # 直到t1 和 t2 都执行完成，才会往下执行
    t1.join()
    t2.join()
    print("End at:", time.ctime())


if __name__ == "__main__":
    main()
    while True:
        time.sleep(10)