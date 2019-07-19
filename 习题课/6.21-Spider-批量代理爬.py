# -*- coding:utf-8 -*-
# @Time  ：2019/6/21 0:32
# @Author: Athany
# @File  : 6.21-Spider-批量代理爬.py

"""
构建代理集群/队列
每次访问服务器，随机抽取一个代理
抽取可以使用random.choice

"""

# 分析步骤：
# 1、构建代理群
# 2、每次访问，随机选取代理并执行

from urllib import request, error
import random


# 1.设置代理地址
# 列表里存放的是字典类型的元素
proxy_list = [
    {"http": "219.157.146.198:8118"},
    {"http": "111.13.134.22:80"},
    {"http": "39.137.77.66:8080"},
    {"http": "111.13.134.23:80"},

]

# 2.创建ProxyHandler
proxy_Handler_list = []
for proxy in proxy_list:
    proxy_Handler = request.ProxyHandler(proxy)
    proxy_Handler_list.append(proxy_Handler)

# 3.创建opener
opener_list = []
for proxy_Handler in proxy_Handler_list:
    opener = request.build_opener(proxy_Handler)
    opener_list.append(opener)




url = "http://www.baidu.com"

try:
    # 4.安装opener
    opener = random.choice(opener_list)
    request.install_opener(opener)

    rsp = request.urlopen(url)
    html = rsp.read().decode("utf-8")
    print(html)

except error.URLError as e:
    print(e)

except Exception as e:
    print(e)
