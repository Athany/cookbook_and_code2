import threading
import time

num = 0
m = threading.RLock()


class MyThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)

        if m.acquire():
            num = num+1
            msg = self.name+' set num to '+str(num)
            print(msg)
            m.acquire()
            m.release()
            m.release()


def testh():
    for i in range(5):
        t = MyThread()
        t.start()


if __name__ == '__main__':
    testh()
