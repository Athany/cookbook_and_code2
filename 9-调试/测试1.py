def myF2():
    def myF3():
        print("In myF3")
        def myF4():
            print("运行到我这儿了吗？")
            return 5
        return myF4
    return myF3

a = myF2()
a

print("*" * 10)



def myF2():
    def myF3():
        print("In myF3")
        def myF4():
            print("运行到我这儿了吗？")
            return 5
        return myF4
    return myF3

a = myF2()

print(a)

print("*" * 20)

def myF2():
    def myF3():
        print("In myF3")
        def myF4():
            print("运行到我这儿了吗？")
            return 5
        return myF4
    return myF3

a = myF2()

print(a()())

print("*" * 30)

def myF2():
    def myF3():
        print("In myF3")
        def myF4():
            print("运行到我这儿了吗？")
            return 5
        return myF4
    return myF3

a = myF2()

print(a())