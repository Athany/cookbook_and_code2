
# 包含一个学生类
# 一个sayHello函数
# 一个打印语句

class Student():

    def __init__(self, name="NoName", age=18):
        self.name = name
        self.age = age

    def say(self):
        print("My name is {0}".format(self.name))


def sayhello():
    print("Hi,见到你很高兴！")

# 此判断语句建议一直作为程序的入口，也就是第一句被执行的代码
if __name__ == "__main__":
    print("我是模块p01，你在叫我吗？")