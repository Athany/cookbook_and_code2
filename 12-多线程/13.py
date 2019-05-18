# encoding=utf-8
import threading
import time

# Python2
# from Queue import Queue
# Python3
import queue


class Producer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            # qsize返回queue内容长度
            if queue.qsize() < 1000:
                for i in range(100):
                    count = count + 1
                    msg = self.name+'生成产品'+str(count)
                    # put是往queue中放入一个值
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)


class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() > 100:
                for i in range(3):
                    # get是从queue中取出一个值
                    msg = self.name + '消费了 '+queue.get()
                    print(msg)
            time.sleep(1)


if __name__ == '__main__':
    queue = queue.Queue()

    for i in range(500):
        queue.put('初始产品'+str(i))    # 在queue中先放进去了初始产品0-499号，消费者消费时优先消费这些，然后再消费生产者生产出后放入的生产产品第多少多少个。
    for i in range(2):
        p = Producer()                 # 设立两个生产者
        p.start()
    for i in range(5):                 # 设立了5个消费者
        c = Consumer()
        c.start()
