# -*- coding:utf-8 -*-
# 委派生成器
from collections import namedtuple
"""
解释：
    1、外层for 循环每次迭代会新建立一个grouper 实例，赋值coroutine变量；
    2、激活协程
    3、内层for循环变量字典value值，并将该value发送给协程，进行平均值计算；
    4、发送哨兵，终止协程，打印计算结果
"""

ResClass = namedtuple("Res", "count average")


# 子生成器
def averager():
        total = 0.0
        count = 0
        average = None

        while True:
            term = yield
            if term is None:
                break
            total += term
            count += 1
            average = total / count
        return ResClass(count, average)


# 委派生成器
def grouper(storages, key):
    while True:
        # 获取averager()返回值
        storages[key] = yield from averager()


# 客户端代码
def clinet():
    process_data = {
        'boys_1': [20, 18, 12, 32, 333, 43, 432],
        'boys_2': [123, 321, 32123, 3223, 423, 4232, 23]
    }

    storages = {}

    for k, v in process_data.items():
        # 获得协程
        coroutine = grouper(storages, k)

        # 预激协程
        next(coroutine)
        # 发送数据到协程
        for dt in v:
            coroutine.send(dt)

        # 终止协程
        coroutine.send(None)
    print(storages)


# run
clinet()
