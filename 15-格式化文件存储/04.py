import xml.etree.ElementTree as et

stu = et.Element("Student1")
name = et.SubElement(stu, "Name")
name.attrib = {"lang": "en"}
name.text = "aimmon"
age = et.SubElement(stu, "Age")
age.text = '19'  # int 会提示不能序列化
et.dump(stu)
