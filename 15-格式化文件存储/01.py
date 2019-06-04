# -*- coding:utf-8 -*-
import xml.dom.minidom
# 负责解析xml文件
from xml.dom.minidom import parse

# 使用parse 打开xml 文件
DOMTREE = xml.dom.minidom.parse("Student.xml")
# 得到文档对象
doc = DOMTREE.documentElement

print(type(doc))
# 显示子元素
for ele in doc.childNodes:
    if ele.nodeName == 'Teacher':
        print("------------Node:{0}--------------".format(ele.nodeName))
        childs = ele.childNodes
        print(childs)
        for child in childs:
            if child.nodeName == 'Name':
                # data 是本节点的一个属性,表示值
                print("Name:{0}".format(child.childNodes[0].data))

            if child.nodeName == "Mobile":
                print("Mobile:{0}".format(child.childNodes[0].nodeValue))

            if child.nodeName == "Age":
                print("Age:{0}".format(child.childNodes[0].data))
                if child.hasAttribute("Detail"):
                    print("age_detail :{0}".format(child.getAttribute("Detail")))