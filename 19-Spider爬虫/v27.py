from bs4 import BeautifulSoup
import html5lib

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
# print(soup)
# print(type(soup))
# 格式化
# print(soup.prettify())
# 标签选择
print('soup.title 输出：', soup.title)
# 打印第一个
print('soup.p 输出：', soup.p)
# 获取文本内容
# get_text() 获取当前标签下，子孙标签的所有文本
print('soup.i.get_text() 输出：', soup.i.get_text())
# string只能获取当前标签下的文本
print('soup.i.string 输出：', soup.i.string)
print('soup.i.text 输出：', soup.i.text)
# 标签属性
print('soup.title.name 输出：', soup.title.name)
# attrs所有的属性，字典字典{"属性名"：[值]}
print('soup.p.attrs 输出：', soup.p.attrs)
# 访问属性
print("soup.p.attrs['class'] 输出：", soup.p.attrs['class'])
# 直接访问属性
print("soup.p['class'] 输出：", soup.p['class'])
# 获取父节点
print("soup.p.parent 输出：", soup.p.parent)
# 获取祖父节点
# print("soup.p.parents 输出：",soup.p.parents)
