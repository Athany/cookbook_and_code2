from bs4 import BeautifulSoup
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

# css选择器
# 查找id为story下的a(子孙节点)
print(soup.select("#story a"))
# 查找id为story下的子节点下的a(子节点)
print(soup.select("#story > i > a"))
