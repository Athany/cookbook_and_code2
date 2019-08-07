# -*- coding:utf-8 -*-
# @Time  ：2019/8/3 22:51
# @Author: Athany
# @File  : 01_Spider.py

from urllib import request

url = "http://www.baidu.com"

rsp = request.urlopen(url)
print(rsp)
content = rsp.read().decode()
print(content)


# w3school 资料简单爬取
# 
