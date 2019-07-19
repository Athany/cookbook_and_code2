# -*- coding:utf-8 -*-
# @Time  ：2019/7/11 22:22
# @Author: Athany
# @File  : 7.11-Spider- etree练习糗事百科.py

"""
爬取糗事百科
分析：
1. 需要用到requests爬取页面，用xpath，re来提取数据
2. 可提取信息：用户头像链接，段子内容，点赞次数
3. 保存到json文件中

大致分三部分：
1. down页面
2. xpath提取信息
3. 保存文件，落地
"""

import requests
from lxml import etree


url = "https://www.qiushibaike.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9"
}

rsp = requests.get(url, headers=headers)
html = rsp.text

# 把页面解析成html
html = etree.HTML(html)
print(html.text)
rst = html.xpath('//div[contains(@id, "qiushi_tag")]')
print(rst)

for r in rst:
    print(r)
    content = r.xpath('//div[@class="content"]/span')[0].text.strip().encode('utf-8')
    print(content)
