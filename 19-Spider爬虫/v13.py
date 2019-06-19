#-*- coding:utf-8 -*-

from urllib import request

if __name__ == '__main__':
    url = "http://www.renren.com/223554497/profile"

    headers = {
        # Cookie写的是网页中F12打开，然后看Cookie信息
        "Cookie": "ick_login=0a9a8207-74be-461f-a3d3-63400cb46278; anonymid=jwp43nbr-d392yz; \
                    depovince=GW; _r01_=1; jebecookies=1595d62f-84bc-4129-abc8-5bafc020f5b9|||||; \
                    _de=520A9431D662BFBC7900C17307811BC25212E40F3D18115C; p=94d99880f8c20c5789815424cd2504b67; \
                    first_login_flag=1; ln_uact=zilang200609@163.com; \
                    ln_hurl=http://hdn.xnimg.cn/photos/hdn121/20090910/1115/main_e1Bs_7283d019117.jpg; \
                    t=622afd799174a2f3c4f45206067f642b7; societyguester=622afd799174a2f3c4f45206067f642b7; \
                    id=223554497; xnsid=c31b2d04; ver=7.0; loginfrom=null; wp_fold=0"
    }

    req = request.Request(url, headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode("utf-8")

    with open("rsp2.html", "w", encoding="utf-8") as f:
        f.write(html)
