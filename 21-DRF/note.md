# Django REST Framework
## 前后端分离的历史：
·完全内嵌时代
        早年，脚本语言是内嵌到HTML内实现逻辑控制的，实现小项目时尚可应付，
        但是一旦项目膨胀，业务逻辑越来越多，这种脚本代码和HTML源码混杂在一起的
        做法就会让前端网页设计师抓狂，可读性变得越来越差，维护成本也开始增加。

·模版时代
        页面中那些需要更新的内容，用标签留白，后端程序向指定标签传送数据，
        这个过程称为“渲染”，整个逻辑和做“填空题”很类似。但是，由于前后端人员
        仍然需要维护同一个HTML文件，导致许多业务逻辑还是不能做到很清晰。

·API时代
        今天，脚本代码和HTML代码更进一步地分离，前后端通过Ajax和JSON互传数据，
        对于前端设计师来说，他们只关注与页面和数据（规范化之后的JSON），而不需要
        关注逻辑，而后端彻底和HTML页面解耦，他们之间唯一的衔接点就是API的制定和联调。

·API (Application Programming Interface, 应用程序编程接口)
    ·目的：为了应付千变万化的业务需求
·REST (Representational State Transfer)，具象状态转移
    ·由Roy Fielding博士在2000年他的博士论文中提出来的一种软件架构风格
    ·RESTful : 遵循REST规范技术设计的软件都可以成为RESTful
·REST规范
    ·URL代表一个资源，一个资源应该是一个名词
    ·动作由HTTP的method方法提供
    ·= URL应该包含版本信息，版本信息也可以放在HTTP协议中
    ·过滤信息：使用URL的参数代表参数
    ·返回值：每一个返回码都有具体的特定含义
    ·返回格式：推荐固定具体格式
·Django REST Framework （DRF）DRF文档：
    ·https://q1mi.github.io/Django-REST-framework-documentation/
    ·安装：pip install djangorestframework
    ·版本问题：version3.7是基于1.xx版本的django, 之后是2.xx版本的django
    ·django_filter 依赖的是 djangorestframework 3.7
·DRF的主要任务：彻底分离前后端, 快速开发RESTful风格的API
    ·案例YlxyDRF
## 2. 序列化/反序列化
·序列化：把系统运行中的一些实例等转换成一种可直接表示出来的格式，用来保存，传输等
·反序列化：序列化的反向操作
·serializer(序列化器) 的类型参数
    ·read_only : 仅用于序列化输出
    ·write_only: 反序列化输入
    ·required: 反序列化时必须输入，默认是True
    ·allow_null : 允许传入None
    ·validators : 使用验证器
·创建serializer对象/使用
    ·构造方法
        Serializer(instance=None,data=empty,**kwarg)
    ·一个最简单的例子(完整版)：DRF
        ·1.创建Project和APP: 
            django-admin startproject DRF 
            python manage.py startapp MySel   
        ·2.然后需要把DRF作为一个app装载进系统，修改settings.py:
        
            INSTALLED_APPS = (
                'django.contrib.admin',
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.messages',
                'django.contrib.staticfiles',
                'rest_framework', # 把DRF安装上
                'MySel',
            )
   ·3.创建模型Student，修改models.py：
   
            class Student(models.Model):
                name = models.CharField(max_length=5)
                age = models.IntegerField()
                score = models.IntegerField()
                
   4.设置序列化器（serializer）在MySel目录下新建一个文件serializers.py，输入以下内容：
   
            from rest_framework import serializers
            class StudentSerializer(serializers.Serializer):
                name = serializers.CharField(label='姓名', max_length=5)
                age = serializers.IntegerField()
                score = serializers.IntegerField()
   数据迁徙：
   
            python manage.py makemigrations 
            python manage.py migrate
   进入shell测试：
    python manage.py shell      
    
            from MySer.models import Student
            from MySer.serializers import *
            stus = Student.objects.all()
            # 先添加两行数据
            stu=Student()
            stu.name='刘晓娜'
            stu.age=12
            stu.score=78
            stu.save()
            stu=Student()
            stu.name='刘大拿'
            stu.age=19
            stu.score=90
            stu.save()
            ser = StudentSerializer(stus[0]) #将对象stus[0]送入序列化器
            ser.data
            显示：{'name': '刘晓娜', 'age': 12, 'score': 78}
            # 上例是把一个对象序列化，下面是多个对象（many=True）
            ser = StudentSerializer(stus,many=True)
            ser.data
            显示：[OrderedDict([('name', '刘晓娜'), ('age', 12), ('score', 78)]), 
            OrderedDict([('name', '刘大拿'), ('age', 19), ('score', 90)])]
   创建视图聚合（Views）