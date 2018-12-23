# 利用time函数，生成两个函数，顺序调用，计算总的运行时间
import time
import _thread as thread


def loop1():
    # ctime得到当前时间
    print("Start loop 1 at:", time.ctime())
    # 睡眠时间
    time.sleep(4)
    print("End loop 1 at:", time.ctime())


def loop2():
    # ctime得到当前时间
    print("Start loop 2 at:", time.ctime())
    # 睡眠时间
    time.sleep(2)
    print("End loop 2 at:", time.ctime())


def main():
    print("Start at:", time.ctime())
    # 启用多线程去执行两个函数
    # 写法为start_new_thread
    # 后面的括号必须有，用于放参数
    thread.start_new_thread(loop1, ())
    thread.start_new_thread(loop2, ())
    print("End at:", time.ctime())


if __name__ == "__main__":
    main()
    while True:
        time.sleep(10)
    # 此处循环，是为了在上述两个线程完成之前，主线程要等待，不然主线程会直接继续工作，其他两个线程没有主线程运行的快，无法输出结果。