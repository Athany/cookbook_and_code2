# 1.模块
· 一个模块就是一个包含Python代码的文件，后缀名称是.py就可以，模块就是一个Python文件
· 为什么要用模块
    · 程序太大，编写维护非常不方便，需要拆分
    · 模块可以增加代码重复利用的方式
    · 当做命名空间使用，避免命名冲突
· 如何定义模块
    · 模块就是一个普通文件，所以任何代码都可以正常书写
    · 不过根据模块的规范，最好在模块中编写以下内容
        · 函数（单一功能）
        · 类（相似功能的组合，或者类似业务模块）
        · 测试代码

· 如何使用模块
    · 模块直接导入
        · 假如模块名称以数字开头，需要借助importlib帮助
    · 语法
        
        import module_name
        module_name.function_name
        module_name.class_name
     · 案例 01，02，p01，p02  
    
   · import 模块 as 别名
        ·导入的同时直接给模块起一别名
        · 其余用法不变
        · 案例p03
    
   · from module_name import func_name, class_name
        ·按照上述方法有选择性的导入
        ·使用的时候可以直接使用导入的内容，不需要前缀
        ·案例p04
        
   · from module_name import *
        · 导入模块的所有内容
        ·案例p05
     
   · 'if __name__ == "__main__"' 的使用
        · 可以有效避免模块代码被导入的时候被动执行的问题
        · 建议所有程序的入口都以此为入口
        
# 模块的搜索路径和储存
· 什么是模块的搜索路径
    · 加载模块的时候，系统会在哪些地方寻找此模块
· 系统模块的默认路径

        import sys
        sys.path 属性可以获取路径列表
       ·案例p06  
        
· 添加搜索路径

        sys.path.append（dir）
        
· 模块的加载顺序
    · 搜索内存中已经加载好的模块
    · 搜索Python的内置模块
    · 搜索 sys.path路径
    
# 包
· 包是一种组织管理代码的方式，包里存放的是模块
· 用于将模块包含在一起的文件夹就是包
· 自定义包的结构

        |---包
        |---|--- __init__.py  包的标志文件
        |---|--- 模块1
        |---|--- 模块2
        |---|--- 子包(子文件夹)
        |---|---|--- __init__.py  包的标志文件
        |---|---|--- 子包模块1
        |---|---|--- 子包模块2


· 包的导入操作
    · import package_name
        · 直接导入一个包，可以使用__init__.py 内的内容
        · 使用方法是：
        
                package_name.func_name
                package_name.class_name.func_name()  
        · 此种方式访问的内容是__init__.py 内的内容
        · 案例pkg01，p07.py  
        
   · import package_name as P
        · 具体用法跟作用方式，跟上述简单导入一致 
        · 注意的是此种方法是默认导入__init__.py的内容
    · import package_module
        ·导入包中的某个模块
        ·使用方法
            
            package.moduel.func_name   
            package.moduel.class_fun()
            package.moduel.class.var
         ·案例 p08.py
   · import package.module as pm
    
· from...import 导入
    · from package import module1, module2, module3, ...
    · 此种方法导入不执行__init__内的内容
             
             from pgk01 import p01
             p01.sayHello()
            
           
   · from package import *
        ·导入当前包 '__init__.py'文件中中的所有函数和类 
        ·使用方法：
        
                func_name()
                class_name.func_name()
                class_name.var
             ·案例p09.py，注意此种导入的具体内容      
                
   · from package.module import *
    ·导入包中指定的模块的所有内容
    ·使用方法
    
            func_name()
            class_name.func_name()
            
            
· 在开发环境中经常会用到其他模块，可以在当前包中导入其他模块中的内容
    · import 完整的包或者模块的路径
· __all__ 的用法
    ·在使用from package import * 的时候， * 可以导入的内容
    · __init__.py 内容为空，或者没有__all__ 那么只可以把__init__.py中的内容导入
    · __init__.py 如果设置了__all__的值，那么按照__all__指定的子包或者模块进行加载 如此则不会载入`__init__`中的内容
    · __all__=['module1', 'module2', 'package1'.........]
    
    
# 命名空间
· 用于区分不同位置不同功能但相同名称的函数或者变量的一个特定前缀
· 作用是防止命名冲突

        setName()
        Student.setName()
        Dog.setName()
    