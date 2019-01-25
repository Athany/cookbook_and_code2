'''
URLError的使用
'''
from urllib import request, error

if __name__ == '__main__':

    # 一个不存在的连接
    url = "http://www.baidu.com/oooooo"

    try:
        req = request.Request(url)
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)
    except error.URLError as e:
        if hasattr(e, 'code'):
            print("HTTPError")
            print(e.code)
        elif hasattr(e, 'reason'):
            print("URLError")
            print(e.reason)
