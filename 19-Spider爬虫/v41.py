from urllib import  request
from bs4 import BeautifulSoup
import re
url = "http://www.baidu.com"

rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content,"lxml")
print(soup.name)
print("=="*12)
for node in soup.head.contents:
    if node.name == "meta":
        print(node)
    if node.name == "title":
        print(node.string)


print("=="*33)
tags = soup.find_all(re.compile("^me"),content="always")
for tag in tags:
    print(tag)

