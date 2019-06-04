# -*- coding:utf-8 -*-
import xml.etree.ElementTree as et

tree = et.parse(r'to_edit.xml')

root = tree.getroot()

print(root)
for e in root.iter('Name'):
    print(e.text)

for stu in root.iter("Student"):
    name = stu.find("Name")
    print("name===", name.text)
    if name != None:
        name.set('test', name.text * 2)

stu = root.find("Student")

# 生成一个新额元素
e = et.Element("Adder")
e.attrib = {'a': "b"}
e.text = "我加的"
stu.append(e)

tree.write("to_edit.xml")
