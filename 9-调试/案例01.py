

def sayHello(name):

    print("我想和你说hello，{0}".format(name))
    print("hello" + name)
    print("Done")
    return "******"

if __name__ == "__main__":
    print("*"*30)
    name = input("请输入姓名：")
    print(sayHello(name))
    print("*" * 20)