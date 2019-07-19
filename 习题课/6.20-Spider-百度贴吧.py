# -*- coding:utf-8 -*-
# @Time  ：2019/6/20 21:52
# @Author: Athany
# @File  : 6.20-Spider-百度贴吧.py


"""
爬去百度贴吧-张继科吧
1.张继科吧主页是  https://tieba.baidu.com/f?kw=张继科
2.进去之后，贴吧有很多页
    第一页的网址是 https://tieba.baidu.com/f?kw=张继科&ie=utf-8&pn=0
    第二页的网址是 https://tieba.baidu.com/f?kw=张继科&ie=utf-8&pn=50
    第三页的网址是 https://tieba.baidu.com/f?kw=张继科&ie=utf-8&pn=100
    第四页的网址是 https://tieba.baidu.com/f?kw=张继科&ie=utf-8&pn=150
    第五页的网址是 https://tieba.baidu.com/f?kw=张继科&ie=utf-8&pn=200

3.由上面网址可以找到规律，每一页只有后面的数字不同，且页数应该是（页数-1）*50

解决方法：
1.准备构建参数字典
2、使用parse构建完整的url
3、使用for循环下载

"""

from urllib import request, parse
import time


# 1.准备构建参数字典
qs = {
    "kw": "张继科",
    "ie": "utf-8",
    "pn": 0
}

# 2、使用parse构建完整的url
# 假定只需要前十页
urls = []
baseurl = "https://tieba.baidu.com/f?"

for i in range(10):
    # 构建新的qs
    pn = i*50
    qs["pn"] = str(pn)
    # 把qs编码后和基础url拼接得到完整的url添加到url列表里
    urls.append(baseurl + parse.urlencode(qs))

# 3、使用for循环下载

for url in urls:
    rsp = request.urlopen(url)
    # print(rsp.read())
    html = rsp.read().decode("utf-8")
    print(url)
    # print(html)

    f = open(str(urls.index(url)) + ".html", "wb")
    f.write(html.encode("utf-8"))  # 这儿记得编码
    f.close()
    print("保存完毕")
    time.sleep(1)


if __name__ == '__main__':
    print("程序结束！")
