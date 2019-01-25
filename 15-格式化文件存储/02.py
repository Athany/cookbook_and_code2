import xml.etree.ElementTree

root = xml.etree.ElementTree.parse("Student.xml")
print("利用getiterator 访问...")
nodes = root.getiterator()
for node in nodes:
    print("...{}...{}...".format(node.tag, node.text))

print("利用find 和findall 方法...")
ele_teacher = root.find("Teacher")
print(type(ele_teacher))
print("----{}---{}---".format(ele_teacher.tag, ele_teacher.text))

ele_stu = root.findall("Student")
print(type(ele_stu))
for ele in ele_stu:
    print("======={}===={}==".format(ele.tag, ele.text))
    for sub in ele.getiterator():
        print(sub.tag, ">>>", sub.text)

        if sub.tag == "Name":
            print(sub.attrib.keys(), "<<<<", sub.text)
