# -*- coding:utf-8 -*-
# @Time  ：2019/6/2 21:49
# @Author: Athany
# @File  : 6-2用协程的方式，修改播放电影和音乐的练习.py

import asyncio
import threading

async def sum(a, b):
    print("现在开始准备计算，当前线程是：{}。".format(threading.currentThread()))
    r = int(a) + int(b)
    await asyncio.sleep(1)
    print("计算已经结束，当前线程是：{}。".format(threading.currentThread()))
    return r


loop = asyncio.get_event_loop()
task = asyncio.gather(sum(1, 2), sum(3, 4))
loop.run_until_complete(task)
r1, r2 = task.result()
print(int(r1) * int(r2))
loop.close()
