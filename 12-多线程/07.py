import time
import threading
def fun():
    print("Start fun")
    time.sleep(2)
    print("End fun")

print("Main thread")
t1 = threading.Thread(target=fun,args=())
t1.setDaemon(True)
# t1.daemon = True
t1.start()
time.sleep(1)
print("Main thread end")