# -*- coding:utf-8 -*-
# @Time  ：2019/7/11 20:40
# @Author: Athany
# @File  : 7.11-Spider-cookie猫眼电影.py

"""
1.url : https://maoyan.com/board
2. 把电影信息尽可能多的拿下来

分析
1.一个影片的内容是以dd开始的单元
2. 对应找到每一个dd，用re挨个查找需要的信息

方法就是三步走：
1. 把页面down下来
2. 提取出dd单元为单位的内容
3. 对每一个dd，进行单独信息提取
"""

from urllib import request

# 1.把页面下载下来
url = "https://maoyan.com/board"
rsp = request.urlopen(url)
html = rsp.read().decode()

# print(html)

# 2.按照dd提取出内容来，缩小处理范围
import re

s = r"<dd>(.*?)</dd>"

pattern = re.compile(s, re.S)
films = pattern.findall(html)
print(len(films))
# print(films)

# 3.从每一个dd中单独提取出需要的信息
for film in films:
    # 提取电影名称
    s = r'<a.*?title="(.*?)"'
    pattern = re.compile(s)
    title = pattern.findall(film)[0]
    print(title)


