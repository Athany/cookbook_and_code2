import time
import _thread as thread


def loop1(in1):
    # ctime得到当前时间
    print("Start loop 1 at:", time.ctime())
    print("我是参数", in1)
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
    # 写法为start_new_thread
    # 后面的括号必须有，用于放参数
    thread.start_new_thread(loop1, ("aaa",))
    thread.start_new_thread(loop2, ("zsj", "zx"))
    print("End at:", time.ctime())


if __name__ == "__main__":
    main()
    while True:
        time.sleep(10)
