import lxml
from lxml import etree

html_doc = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <ul>
        <li id='l1' class="liClass">1</li>
        <li id='l2'>2</li>
        <li class="liClass">3</li>
        <li id='l4'>4</li>
        <li class="liClass">5</li>
    </ul>
    <div class="liClass">
    </div>
</body>
</html>
'''

mytree = lxml.etree.HTML(html_doc)
# ElementTree object
print(mytree)
print(mytree.xpath('/html/text()'))
print(mytree.xpath('/ul'))
# / 从根元素开始，相当于绝对路径
print(mytree.xpath('/html/body/ul'))
# // 全局搜索，找到所有
print(mytree.xpath('//li'))
ul = mytree.xpath('//ul')
# . 当前
# 返回的都是列表，查找到所有
li = ul[0].xpath('./li')
print(li)

for l in li:
    # 获取属性id的值 @id
    print(l.xpath('./@id'))

# 定位 /标签[@属性='值']
liClass = mytree.xpath("//li[@class='liClass']")
print(liClass)
# 判断，@属性='值' --->返回True或False
print(mytree.xpath("//li/@id='12'"))
print("===========================")
# 直接使用下标访问，下标从1开始 获取对个li里面的文本
print(mytree.xpath('//li[2]/text()'))
# last()最后一个
print(mytree.xpath('//li[last()]/text()'))
# 倒数第二个
print(mytree.xpath('//li[last()-1]/text()'))
# position() 位置 > < = >= <=
print(mytree.xpath('//li[position()>1]'))
# * 通配
print(mytree.xpath('//*[@class="liClass"]'))
# 或 |
print(mytree.xpath('//li[@class="liClass"] | //div[@class="liClass"]'))
