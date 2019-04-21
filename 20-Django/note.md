# Django系统
·环境
    ·python3.6
    ·django1.8
·参考资料
    ·[Django中文教程]（https://yiyibooks.cn/xx/django_182/index.html）
    ·[Python 新手使用 - Django 架站的16堂课]（实体书）
# 环境搭建
·anaconda + pycharm
·anaconda使用
    ·conda list : 显示当前环境安装的包
    ·conda env list : 显示安装的虚拟环境列表
    ·conda create -n envname python=3.6 如:conda create -n tldjango python=3.6
    ·激活conda的虚拟环境
        ·source activeate env_name (Linux下激活)
        ·conda activate envname (Windows下激活) 如: conda activate tldjango
        ·激活的含义是:进入某环境专用命令行界面, 并针对该环境进行设置

·Django安装:
    ·conda activate tldjango (首先激活Django的环境, PS:激活后命令行前面回带一个(tldjango)这样的前缀)
    ·pip install django==1.8
# 后台流程

# 创建第一个Django程序
·django-admin startproject tulingxueyuan (创建Django项目: tulingxueyuan)
# 命令行启动:
·cd tulingxueyuan
·python manage.py runserver (启动服务器)
# PyCharm启动
·1.配置python环境:
    ·点击File菜单 -> Settings -> Project:Python -> Project Interpreter-> “小齿轮”图标 -> ADD -> Conda Environment -> Existing environment-> “...” 图标 ->
        ·Linux系统: Anaconda安装路径下的/envs/相应的虚拟环境名称/bin/python.sh
        ·Windows系统： 1、 C:\Users\用户名\Anaconda3\envs\相应的虚拟环境名称\python.exe 2、 C:\ProgramData\Anaconda3\envs\相应虚拟环境名称\python.exe 3、 C:\Users\rocka.conda\envs\相应虚拟环境名称\python.exe Windows情况有点特殊，我分别在以上三个位置找到过。
        ·注意：刚刚配置好的环境，PyCharm还会把各种包整理一下，当IDE主界面右下方有一条细细的进度条在跑的时候，说明环境还在Update中尚未准备就绪，程序中某些import 包的语句还会被语法提示器认为是错误语句，此时要耐心等待。
·2.配置manage.py文件:
    ·鼠标指向manage.py文件-> 直接点运行 -> 将会报错
    ·此时需要点界面右上角下拉菜单(位于启动按钮左边) -> 选 Edit Configurations ->在Parameters输入参数: runserver -> 确定 -> 出来后点运行即可
# 路由系统 - urls
·创建app
    ·app: 负责一个具体业务或者一类具体业务的模块
    ·python manage.py startapp teacher (在app根目录下执行,生成一个teacher的目录,即teacher路由)
·路由
    ·按照具体的请求url, 导入到相应的业务
    ·django的信息控制中枢
    ·本质上就是接受URL和相应的处理模块的一个映射
    ·在接受URL请求的匹配上使用了RE
    ·URL的具体内容在urls.py文件中 (阅读该文件的代码,发现内部是使用正则在处理URL和对应模块的对应关系)
·需要关注的两点:
    ·接受的URL是什么, 即如何用RE对传入的URL进行匹配
    ·已知URL匹配到哪个处理模块
·URL匹配规则:
    ·从上到下一个一个比对
    ·URL格式是分级格式,则按照级别一级一级往下比对,主要对应URL包含子URL的情况
    ·子URL一旦被调用,则不会返回到主URL
        ·'/one/two/three/'
    ·正则以r开头, 表示不需要转义, 注意尖号(^)和美元符号(\$)
        ·'/one/two/three' 配对正则: r'^one/'
        ·'/oo/one/two/three' 不配对正则: r'^one/'
        ·'/one/two/three/' 配对正则: r'^three/\$
        ·'/oo/one/two/three/oo/' 不配对正则: r'three/\$'
        ·第一个反斜杠并不需要(系统自动忽略)
    ·如果从上到下都没有找到合适的匹配内容,则报错
# 2. 正常映射
·把某一个符合RE的URL映射到事务处理函数中去
·举例如下： from showeast import views as sv urlpatterns = [ url(r'admin/',adming.site.urls), url(r'^normalmap/', sv.normalmap), ]
# 3.URL 中带参数映射
·在多事件处理代码中需要由URL传入参数，形如/myurl/param中的param
·参数都是字符串形式，如果需要整数等形式需要自行传唤
·统称的形式如下: > /search/page/432 中的432需要经常性变化内容，就是参数

·一个较为复杂的例子： > url(r'^withparam/(?P<year>[0-9])/(?P<month>[0,1][0-9)',tv.withparam)
    ·尖号表示从字符串左边第一个字符开始匹配
    ·圆括号表示的是一个参数，里面的内容作为参数传递给被调用的函数 参数名称以问号加大写P开头吗，尖括号里面就是参数的名字 后面花括号表示出现的次数，此处的4 表示只能出现4个0-9的数字
# 4. URL在APP中处理
如果所有应用URL都集中在tulingxueyuan/urls.py中,可能导致文件臃肿 可以把urls具体功能逐渐分散到每个app中 - 从djanco.conf.urls导入include - 注意此时RE部分的写法 - 添加include 导入 - 使用方法: 确保include被导入 - 在根目录的urls.py中写url (1个功能模块只对应1个url) - 写子路由 (功能模块里的子模块,在各自的文件夹内的:模块名_url.py内添加) - 编写各个功能模块的views函数,包括各个子路由的views函数 - 与直接在主urls.py中写理由一样,分散在各个模块文件夹下面写独立的子路由,同样可以使用参数

# 5. URL中嵌套参数
·捕获某个参数的一部分
·例如URL /index/page-3 , 需要捕获数字3作为参数
    ·url(r'index_1/(page-(\d+)/)?$, sv.myindex_1)
    ·url(r'index_2/(?:page-(?P\d+)/)?$', sv.myindex_2)
    ·url(r'^book/page-(?P\d)/$', sv.myindex_2)
    ·以上就是指从一个参数中再提炼一个参数(我个人认为第三个正则更简单明了一些)
# 6. 传递额外的参数
·参数不仅仅来自于URL, 还可能是我们自己定义的内容 url(r'extrem/$',sv.extremParam,{'name':'liuying'}),
·附加参数同样适用于include语句, 此时对include内所有都添加.
# 7.URL的反向解析 reverse
·防止硬编码
·本质上是对每一个URL进行命名
·以后在编码代码中使用URL的值,原则上都应该使用反向解析
·reverse的好处是,只要给一个路由设好名字, 无论URL怎么变, 都可以用名字来引用,方便,主要用于模版
# VIEWS 视图
# 1. 视图概述
·视图即视图函数,接受WEB请求返回WEB相应的事务处理函数.
·响应指符合http协议要求的任何内容,包括json, string, html等
·本章忽略事务处理, 重点在如何返回处理结果上
# 2. 其他简单视图
·django.http为我们提供了很多和HttpResponse类似的简单视图, 通过查看django.http的源代码我们直到.
·此类视图使用方法基本类似,可以通过return语句直反馈给浏览器
·Http404为Exception子类, 所以需要用raise来显式调用
·Debug模式的关闭:
    ·打开根路径下settings.py文件
    ·将Debug = True 改为 False
    ·ALLOWED_HOSTS 改为 "*"
# 3. HttpResponse详解
·方法:
    ·init : 使用页内容实例化HttpResponse对象
    ·write(content) : 以文件的方式写
    ·flush(): 以文件的方式输出缓存区
    ·setcookie(key, value='', maxage = none,expires = None): 设置cookie
        ·key , value 是字符串类型
        ·max_age 是一个整数, 表示在指定秒数后过期
        ·expires 是一个datetime或timedelta对象, 会话将在这个指定的日期/时间过期
        ·max_age 和 expires , 二选一
        ·如果不指定过期时间,则两个星期后过期
        ·delete_cookie(key): 删除指定的key的Cookie, 如果key不存在, 也不会报错
        ·avatar

# 4. HttpRespnseRedirect
·重定向, 服务器端跳转
·构造函数的第一个参数用来指定重定向的地址
·例子: ShowViews/views.py
·在east/urls中添加以下内容: ` url(r'^v101/', views.v101), url(r'^v102/', views.v102), url(r'^v11/"' views.v11, name = "v11"),

# /east/ShowViews/views 中添加以下内容 def v101(request): return HttpRespnseRedirect("/v11") def v102(request): return HttpRespnseRedirect(reverse("v11")) def v11(request): return HttpRespnseRedirect(""这是v11 的返回值") ` avatar

# 5.Request 对象
·Request介绍
    ·服务器接受到http协议的请求后,会根据报文创建HttpRequest对象
    ·视图函数的第1个参数就是HttpRequest对象(在Python中,形参只跟位置相关,而跟具体的参数名无关,例如self亦是如此)
    ·在django.http模块中定义了HttpRequest对象的API
·属性
    ·下面除非特别说明,属性都是只读的 (就像你给张三写一封信, 张三收到后就已经没有修改的意义了)
    ·path : 一个字符串, 表示请求页面的完整路径, 不包含域名
    ·method : 一个字符串,表示使用的HTTP方法,常用时包括:'GET'/'POST'
    ·encoding : 一个字符串,表示提交的数据的编码方式
    ·如果为None则表示使用浏览器的默认设置,一般为utf-8
    ·这个属性是可写的,可以通过修改他来修改访问表单数据使用的编码
    ·GET : 一个类似字典的对象, 包含get请求方式的所有参数
    ·POST : 一个类似字典的对象, 包含post请求方式的所有参数
    ·FILES : 一个类似字典的对象, 包含所有的上传文件
    ·COOKIES : 一个标准的Python字典, 包含所有cookie, 键和值都包含其中
    ·session: 一个即可独有可写的类似于字典的对象,表示当前会话. - 只有当Django启用会话时才可用. - 详细内容见"状态保持".
·方法
    ·is_ajax() : 如果请求是通过XMLHttpRequest发起的,则返回True
·QueryDict 对象 [这个是Django特设的对象,HTTP本身没有]
    ·定义在django.http.QueryDict里
    ·request对象的属性GET, POST都是QueryDict类型的对象
    ·与Python 字典不同,QueryDict类型的对象用来处理同一个键带多个值的情况.
    ·方法get(): 根据键取值
        ·只能获取键的一个值
        ·如果一个键同时拥有多个值,获取最后一个值
    ·方法getlist():根据键获取值
        ·将键的值以列表返回,可以获取一个键的多个值
·GET属性 [此对象对应http协议的GET操作]
    ·QueryDict类型的对象
    ·包含get请求方式的所有参数
    ·与url请求地址中的参数队形,位于?后面
    ·参数的格式是键值对,如key1 = value1
    ·多个参数之间,用&链接,如key1=value1&key2=value2
    ·键是开发人员定下来的,值是可变的
    ·例子: ShowViews/views/v8_get

·POST 属性
    ·QueryDict类型的对象
    ·包含post请求方式的所有参数
    ·与form表单中的空间对应
    ·表单中的控件必须有name属性,name为键,value为值
        ·checkbox存在一键多值的问题
    ·键是开发人员定下来的,值是可变的
    ·例子 ShowViews/views/v9_post
        ·setting中设置模版位置, 在根目录下建立一个templates文件夹,然后在setting.py里修改为: > *('DIRS': [os.path.join(BASE_DIR,"templates")],)
        ·setting中CRSF跨站攻击防护要关闭,此行需要注释掉) > * django.middleware.csrf.CsrfViewMiddleware',
        ·设置get页面的urls和参数 需要在路由文件中添加两个路由: > * url(r'^v9get/', v.v9get), > * url(r'^v9post/', v.v9post),

·手动编写视图
    ·实验目的:
    ·利用django快捷函数手动编写视图处理函数
    ·编写过程中理解视图运行原理
    ·VIEW的目的: 1.. 业务处理 2.. 返回Respongse子类步骤: 1. 拿到模版 2. 拿到数据 3. 环境变量(插入到HTML代码中,以此定位数据填充的位置) 4. 返回
    ·分析:
        ·django把所有请求信息封装入request
        ·django通过URLS模块把相应请求跟时间处理函数链接起来, 并把request作为参数传入.
        ·在相应的处理函数中,我们需要完成两部分
            ·处理业务
            ·把结果封装并返回,我们可以使用简单HttpResponse, 同样也可以自己处理此功能
        ·本例子不介绍业务处理, 把目光集中在如何渲染结果并返回
    ·render(request, templater_name [,context][,context_omstamce][,content_type])
        ·使用模版和一个给定的上下文环境,返回一个渲染后的HttpResponse对象
        ·request: django的传入请求
        ·templater_name : 模版名称
        ·content_instance : 上下文环境
        ·参见例子: teacherapp/views/rendertest
    ·rendertoresponse
        ·根据给定的上下文字典渲染给定模版,返回渲染后的HttpResponse
        ·参见例子: teacherapp/views/render4test

·系统内建视图
    ·系统内建视图,可以直接使用:
    ·404
        ·default.pagenotfound(request, template_name = '404.html')
        ·系统引发Http404时触发
        ·默认窗体request_path变量给模版,即导致错误的URL
        ·DEBUG = True则不会调用404, 取而代之是调试信息
        ·404视图会被传递到一个RequestContext帝乡宁切可以访问模版上下文处理器提供的变量.
    ·500
        ·default.server_error
        ·DEBUG = True 不触发
    ·403
        ·default.permission_denied
        ·DEBUG = True 不触发
    ·500
        ·default.bad_request
        ·DEBUG = True 不触发
# 8. 基于类的视图
·和基于函数的视图的优势和区别:
    ·http方法的methode可以有各自的方法,不需要使用条件分支来解决
    ·可以使用OOP技术(例如Mixin)
·概述
    ·核心是允许使用不同的实例方法来响应不同的HTTP请求方法,而避开条件分支实现
    ·as_view函数作为类的可调用入库,该方法创建一个实例并调用dispatch方法,按照请求方法对请求进行分发,如果该方法没有定义,则引发HttpResponseNotAllowed
·类属性使用
    ·在类定义时直接覆盖
    ·在调用as_view的时候直接作为参数使用,例如: urlpatterns = [ url(r'^about/', GreetingView.as_view(greeting="Greetxxx")), ]
·对基于类的视图的扩充大致有三种方法: Mixin, 装饰as_view, 装饰dispatch
    ·使用Mixin
        ·多继承的一种形式,来自弗雷的行为和属性组合在一起
        ·解决多继承问题
        ·View的子类只能单继承,多继承会导致不可期问题
    ·多继承带来的问题:
        ·结构复杂
        ·优先顺序模糊
        ·功能冲突
    ·解决方法
        ·规格继承 # java interface
        ·实现继承 # python,ruby
·在URLconf中装饰 from django.contrib.auth.decorators import login_required, permission_required from django.views.generic import TemplateView from .views import VoteView urlpatterns = [ url(r'^about/', login_required(TemplateView.as_view(template_name="secret.html"))), url(r'^vote/', permission_required('polls.can_vote')(VoteView.as_view())), ]
·装饰类
    ·类的方法和独立方法不同,不能直接运用装饰器,需要用methode_decorator进行装饰 from django.contrib.auth.decorators import login_required from django.utils.decorators import method_decorator from django.views.generic import TemplateView class ProtectedView(TemplateView): template_name = 'secret.html' @method_decorator(login_required) def dispatch(self, *args, **kwargs): return super(ProtectedView, self).dispatch(*args, **kwargs)
# Models 模型 (ORM)
·ORM
    ·Object Relation Map(对象关系映射) : 把面向对象思想转换成关系数据库思想.操作上把类等价于表格
    ·类对应表格
    ·类中的属性对应表中的字段
    ·在应用中的models.py文件中定义class
    ·所有需要使用ORM的class都必须是 models.Model 的子类
    ·class中的所有属性对应表格中的字段
    ·字段的类型都必须使用 models.xxx 不能使用python中的类型
    ·在django种，Models负责跟数据库交互 avatar
# Django 链接数据库
·自带默认数据库Sqllite3
    ·关系型数据库
    ·轻量级
    ·建议开发用sqlite3， 部署用mysql之类数据库
    ·切换数据库在settings中进行设置
    ·# 用django 连接 mysql DATABASES = [ 'default' = { 'ENGINE' : 'django.db.backends.mysql', 'NAME' : '数据库名', 'PASSWORD' : '数据库密码', 'HOST' : '127.0.0.1', 'PORT' : '3306', } ]
    ·django 连接 mysql需要在项目文件下的init文件中导入pymysql包
        ·> import pymysql > pymysql.installasMySQLdb()
# models类的创建与使用
·定义和数据库表映射的类
    ·在应用中的models.py文件中定义class [每一个app下面都有这个文件]
    ·所有需要使用ORM的class都必须是 models.Model 的子类
    ·class中的所有属性对应表格中的字段
    ·字段的类型都必须使用 modles.xxx 不能使用python中的类型
·字段常用参数
    ·max_length : 规定数值的最大长度
    ·blank : 是否允许字段为空,默认不允许
    ·null : 在DB中控制是否保存为null, 默认为false
    ·default : 默认值
    ·unique : 唯一
    ·verbose_name : 假名
    ·数据库的迁移（在models里创建类后通知数据库）
    ·在命令行中，生成数据迁移的语句（生成sql语句） > * python manage.py makemigrations
    ·在命令行中，输入数据迁移的指令 > * python manage.py migrate
    ·如果迁移中没有变化或者报错，可以强制迁移 > python manage.py makemigrations 应用名 > python manage.py migrate 应用名
    ·对于默认数据库，为了避免出现混乱，前提是数据库中没有数据，可以删除自定义app下的migrations文件夹和db.sqlites3数据库
    ·如果报错,显示"App 'APP名字' could not be found. Is it in INSTALLED_APPS?", 说明没有在settings.py里注册: INSTALLED_APPS = ( 'django.contrib.admin', 'django.contrib.auth', 'django.contrib.contenttypes', 'django.contrib.sessions', 'django.contrib.messages', 'django.contrib.staticfiles', 'teacher', # 把自定义的app填进去 'orm', )
# 查看数据库中的数据
·1.启动命令行：python manage.py shell 注意点：对orm的操作分为静态函数和非静态函数两种，静态函数是指在内存中类共用的，非静态函数是指每个实例掌握的
·2.在命令行中导入对应的映射类 > * from app名.models import 类名
·一个完整的例子: from teacher.models import Teacher dana = Teacher() dana.name = "Dana" dana.age = 18 dana.address = "北京图灵学院" dana.save() # 保存 ta = Teacher.objects.all() # 返回集合 ta[0].name # 访问name属性,显示: Dana ta[0].age # 访问age属性,显示: 18 ta[0].address # 访问address属性,显示: '北京图灵学院' ta[0].course # 访问course属性,显示为空
·如上操作向Teacher表中增加几条记录之后,用for循环遍历: for t in ta: print("Name: {0}, Age{1},Address:{2},Course:{3}".format(t.name,t.age,t.address,t.course)) 显示结果: Name: Dana, Age18,Address:北京图灵学院,Course: Name: Daozhang, Age45,Address:程度小北路,Course: Name: WangGonh, Age29,Address:,Course:Java
·查询age=45的记录 > ta = Teacher.objects.filter(age=45)
    > ta
    直接输入ta回车,显示ta的内容,age=45的记录只有一个就是daozhang, 显示为:
    []

·3.使用object属性操作数据库，object是模型中实际和数据进行交互的
·4.查询命令
    ·类名.objects.all()查询数据库表中的所有内容，返回的结果是一个QuerySet查询集合类型
    ·类名.object.filter(条件)
    ·常见查找方法
    ·1. 通用查找格式:属性名__条件符号=值
    ·例如, 查找所有age大于18的记录: ta = Teacher.objects.filter(age__gt > 18)
    ·条件符号有：
        ·gt:大于
        ·gte:大于等于
        ·lt:小于
        ·lte:小于等于
        ·range:范围
        ·year:年份
        ·isnull:是否为空
        ·2、查找等于指定值的格式：属性名=值
        ·3、模糊查找：属性名__查找方式=值
        ·查找course中包含字母T的老师
            ·ta = Teacher.objects.filter(course__contains = "T")
        ·查找方式有：
            ·exact:精确等于
            ·iexact:不区分大小写
            ·contains:包含
            ·startwith:以..开头
            ·endwith:以..结尾
# 数据库表关系
·多表联查：利用多个多联合查找某一项信息或者多项信息

·1:1 OneToOne
    ·建立关系:在模型任意一边即可，使用OneToOneField
    ·add: （增）有两种方式：
        ·实例化方法，直接实例化保存
        ·create方法，返回类型是，推荐这种方法
        ·PS: 添加有关系的一边，使用create方法，或者使用实例创建
        ·例如： s = School() s.school_id = 2 s.school_name = "nanjingtulingxueyuan" s.save() #方法1：直接实例化 m =Manager() m.manager_id=10 m.manager_name = "dana" m.my_school=s m.save() #方法2：使用create m = Manager.objects.create(manager_id=20,manager_name="erna",my_school=s)`
    ·query: （查）
        ·由子表查母表（定义关系的表叫子表），由子表的属性直接提取信息： m = Manager.objects.get(manager_name="dana") m m.my_school m.my_school.school_name 'nanjing tulingxueyuan' # 查询成功
        ·又或者可以把上述操作串起来一次性操作： Manager.objects.get(manager_name="dana").my_school.school_name 'nanjing tulingxueyuan' # 查询成功
        ·由母表查子表，使用双下划线： s = School.objects.get(manager__manager_name="dana") s # 查询成功
    ·change:（改）
        ·单个修改后使用save保存 s.school_name = "南京图灵学院" s.save() s # 修改成功
        ·批量修改使用update ss = School.objects.all() ss.update(school_name="图灵学院") ss [, ] # 批量修改成功
        ·无论是对子表还是母表修改方法都一样
    ·delete:直接使用delete删除

·1:N OneToMany
    ·一个表格的一个数据项/对象等，可有很多个另一个表格的数据项
    ·比如，一个学校可有很多个老师，一般一个老师只会在一个学校上课
    ·使用上
        ·使用ForeignKey
        ·在多的那一边，比如上面的例子就是在Teacher表格里进行定义
    ·add: (增)
        ·跟一对一方法类似，通过cerate和new来添加
        ·create:把属性都填满，然后不需要手动保存
        ·new（也就是实例化方法）:可以属性或者参数为空，必须用save保存
    ·query:
        ·以学校和老师举例
        ·如果知道老师，查学校，则通过增加的关系属性，直接使用
        ·例如：查找t1老师是哪个学校的: t1.teacher_name '刘大拿' t1.my_school
    ·反查
        ·由学校，想查下这个学校所有老师，则在学校后跟老师这个类（类名称小写）接下划线set来表示
        ·可以简单理解成teacher_set是School类里的一个隐藏属性
        ·例如，查询1号学校下面有多少个老师： ts = s1.teacher_set.all() ts [, ] ts[0].teacher_name '刘大拿'
        ·又或者精确查找： t = s1.teacher_set.all().filter(teacher_name="刘大拿") t[0].teacher_name '刘大拿'
·N:N ManyToMany
    ·表示任意一个表的数据可以拥有对方表格多项数据，反之亦然
    ·比如典型例子就是老师和学生，老师可以有多个学生，学生也可以有多个老师
    ·使用上，在任意一方，使用ManyToMany定义，只需要定义一边
    ·add:
        ·添加老师，则在Student实例.teachers.add()，也可以用create方法
            ·注意，用实例添加多对多数据，需要两次save s1 = Student() s1.student_name = "aoteng" s1.save() t1 = Teacher.objects.all()[0] s1.teachers.add(t1) s1.save() t = s1.teachers.all() t[0].teacher_name '刘大拿'
    ·query:
        ·跟一对多类似，使用隐含属性set查询 t1 = Teacher.objects.all()[0] ss = t1.student_set.all() ss[0].student_name 'aoteng'
        ·注意：如果想实现双向互查，必须在类代码里面两边都相互添加一行: > models.ManyToManyField s1 = Student.objects.all()[0] tt = s1.teacher_set.all() tt[0].teacher_name '刘大拿'
# 模版（Template）
·模板：一组相同或者相似的页面，在需要个性化的地方进行留白，需要的时候只是用相应数据进行填充
    ·步骤
        1.在settings.py中进行设置:TEMPLATES
        2.在templates文件夹下编写模板并调用   一个最简单的完整的例子：
        3.激活环境： activate tl_django
        4.创建项目： django-admin startproject django_tpl
        5.创建app： python manage.py startapp mytpl
        6.在项目的根目录下建立一个templates的目录
        7.在templates目录下新建一个one.html文件，内容如下：
        Hello World！
        8.编辑Django系统自带的settings.py文件： 找到Templates下的DIR位置，修改为： 'DIRS': [os.path.join(BASE_DIR, "templates")],
        9.为manager.py添加启动变量runserver (仅限Pycharm环境)
        10.编辑Django系统自带的urls.py： 在头部添加包引用：import mytpl.views as v (如果这行Pycharm出红线，就选File菜单的Invalidate Caches/Restart,重启后鼠标单击项目目录，Mark Directory As -> Sources Root) 然后再下方依葫芦画瓢添加一个路由：url(r'^one/', v.one),
        11.打开mytpl下的views.py 在头部添加包引用：from django.http import HttpResponse 添加一个函数one: def one(request): return render(request,r"one.html")
        12.运行manage.py
        13.在浏览器输入：127.0.0.1:8000/one 
## 模板-变量
·变量的表示方法：{{var_name}}
·在系统调用模板的时候，会有相应的数据查找相应的变量名称，如果找到，则填充也叫渲染，否则跳过
·参见例子：two.html
## 模板-标签
·for标签: {% for .. in .. %} 循环语句 {% endfor %}
·参见例子：three.html，显示班级成绩
·
·if标签，用来判断条件 {% if 条件 %} 条件成立执行语句 {% elif 条件 %} 条件成立执行语句 {% else %} 以上条件都不成立执行语句 {% endif %}

参见例子：four.html
## csrf标签,跨站请求伪造
·在提交表单的时候，表单页面需要加上{% csrf_token %}
·参见例子fiveget请求表单地址, fivepost发送表单信息地址
·原理：
    1.浏览器提交一个get请求到服务器，服务器返回一个带csrf_token的form回浏览器
    2.此时浏览器正常提交form，隐含提交了csrf_token
    3.服务器验证这个新提交上来的csrftoken是否刚才服务器自己生成的那个csrftoken?
    4.如果csrf_token不一致，说明本次提交是伪造的
·在settings.py：
    ·'django.middleware.csrf.CsrfViewMiddleware', 是控制csrf_token的开关，
    ·如果此选项关闭，则不对csrftoken进行检查，反之则一定会检查，如果打开了此设置但是在html代码里又不含{% csrftoken %}，则将报错： CSRF token missing or incorrect.
# SESSION
·为了应对HTTP的无协议性
·用来保存用户比较敏感的信息
·他是属于request的一个属性
·常用操作：
    ·request.session.get(key,defaultValue)
    ·request.session.clear():清除全部
    ·request.session[key] = value : 赋值
    ·request.session.flush() : 删除当前会话并清除会话的cookie
    ·del request.session[key]
# 分页
·django提供现成的分页器用来对结果进行分页 
·from django.core.paginator import Paginator    
