import multiprocessing
from time import sleep, ctime


class ClockProcess(multiprocessing.Process):
    """
    两个函数比较重要
    1. init构造函数
    2. run
    """

    def __init__(self, interval):
        super().__init__()
        self.interval = interval

    def run(self):
        while True:
            print("The time is %s" % ctime())
            sleep(self.interval)


if __name__ == '__main__':
    p = ClockProcess(3)   # 定义类时已经申明是多进程的一个子类，所以这儿直接实例化即可
    p.start()

    while True:
        print('sleeping.......')
        sleep(1)
