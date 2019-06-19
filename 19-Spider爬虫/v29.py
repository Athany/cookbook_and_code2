from bs4 import BeautifulSoup
import re
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title title1">
    <ul>
        <li>1</li>
        <li>2</li>
        <li>3</li>
    </ul>
    <em>hello</em>
    <b>The Dormouse's story</b>
    <i>haskdjfhakjsf</i>
</p>
<p class="story" id='story'>
    <i>
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
    </i>
</p>
<p class="story">...</p>
"""
# 用lxml格式解析html 解析器
# soup = BeautifulSoup(html_doc,"lxml")
soup = BeautifulSoup(html_doc, "html5lib")
# 查找全部
# find_all
"""
 参数：name=None, attrs={}, recursive=True,
 text=None,limit=None, **kwargs
"""
# 查找所有符合的标签，返回一个列表
print(soup.find_all('p'))
# 限制输出
print(soup.find_all('a', limit=2))
# 使用正则
print(soup.find_all(re.compile('^p')))
print(soup.find_all(text=re.compile("^L")))
