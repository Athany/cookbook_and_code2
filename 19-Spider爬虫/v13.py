from urllib import request

if __name__ == '__main__':
    url = "http://www.renren.com/965187997/profile"

    headers = {
        # Cookie写的是网页中F12打开，然后看Cookie信息
        "Cookie": ""
    }

    req = request.Request(url, headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()

    with open("rsp.html", "w") as f:
        f.write(html)
