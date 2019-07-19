# -*- coding:utf-8 -*-
# @Time  ：2019/6/21 12:34
# @Author: Athany
# @File  : 6.20-Spider-伯乐在线.py


"""
爬去伯乐在线的美女的联系方式
需要：
1.登陆
2.在登陆和相应声望值的前提下，提取对方的邮箱
"""

from urllib import request, error, parse
from http import cookiejar
import json


def login():
    """
    输入用户名称和密码
    获取相应的登陆cookie
    cookie写文件
    """
    # 1.需要找到登陆入口
    url = "http://date.jobbole.com/wp-login.php"
    # 2.准备登陆数据
    data = {
        "log": "sugsnano",
        "pwd": "123456789",
        # 登陆后重定向地址
        "redirect": "http://date.jobbole.com/4965/",
        "remember": "on"
    }

    data = parse.urlencode(data).encode()

    # 3.准备存放cookie文件
    # r表示不转义
    f = r"jobbole_cookie.txt"

    # 4.准备请求头信息
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chr\
        ome/64.0.3282.119 Safari/537.36",
        "Connection": "keep-alive"


    }

    # 5.准备cookie handler
    cookie_handler = cookiejar.MozillaCookieJar(f)
    # 6. 准备http请求handler
    http_handler = request.HTTPCookieProcessor(cookie_handler)
    # 7.构造opener
    opener = request.build_opener(http_handler)
    # 8.构建请求对象
    req = request.Request(url, data=data, headers=headers)
    # 9.发送请求
    try:
        rsp = opener.open(req)
        cookie_handler.save(f, ignore_discard=True, ignore_expires=True)
        html = rsp.read().decode()
        print(html)

    except error.URLError as e:
        print(e)

def getInfo():
    # 1.确定url
    url = "http://date.jobbole.com/wp-admin/admin-ajax.php"
    # 2.读取已保存的cookie
    f = r"jobbole_cookie.txt"
    cookie = cookiejar.MozillaCookieJar()
    cookie.load(f, ignore_expires=True, ignore_discard=True)
    # 3.构建http_handler
    http_handler = request.HTTPCookieProcessor(cookie)
    # 4.构建opener
    opener = request.build_opener(http_handler)
    # 以下是准备请求对象的过程
    # 5.构建data
    data = {
        "action": "get_date_contact",
        "postId": "4965"
    }

    data = parse.urlencode(data).encode()
    # 6.构建请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36",
        "Connection": "keep-alive"
    }

    # 7.构建请求实体
    req = request.Request(url, data=data, headers=headers)

    # 8.用opener打开
    try:
        rsp = opener.open(req)
        html = rsp.read().decode()

        html = json.loads(html)
        print(html)

        f = "rsp.html"
        with open(f, "w") as f:
            f.write(html)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    login()
