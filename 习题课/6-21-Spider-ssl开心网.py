# -*- coding:utf-8 -*-
# @Time  ：2019/6/21 8:32
# @Author: Athany
# @File  : 6-21-Spider-ssl开心网.py

"""
登陆开心网
利用cookie
免除ssl

"""
# 步骤：
# 1.寻找登陆入口，通过搜索相应文字可以快速定位
# login_url = "https://security.kaixin001.com/login/login_post.php"
# 相应的对应名称，登录名为“loginemail”，密码为“password”
# 2.构造opener
# 3.构造login()
from urllib import request, parse
import ssl
from http import cookiejar

ssl._create_default_https_context = ssl._create_unverified_context
cookie = cookiejar.CookieJar()
cookie_handler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPSHandler()
opener = request.build_opener(cookie_handler, http_handler, https_handler)

def login():
    login_url = "https://security.kaixin001.com/login/login_post.php"

    data = {
        "loginemail": "13119144223",
        "password": "123456"
    }
    # 对post的data进行编码
    data = parse.urlencode(data)
    # 构建request的请求头

    headers = {
        "Content-Length": len(data),
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }

    #构建请求对象
    req = request.Request(login_url, data=data.encode(), headers=headers)
    rsp = opener.open(req)
    html = rsp.read().decode()
    # print(html)

def getHomePage():
    rsp = opener.open(fullurl="http://www.kaixin001.com/home/?_profileuid=181697221")
    html = rsp.read().decode()
    print(html)


if __name__ == '__main__':
    login()
    getHomePage()
