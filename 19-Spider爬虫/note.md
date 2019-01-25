# Python之爬虫准备工作
· 参考资料
    ·python网络数据采集， 图灵工业出版
    ·精通Python爬虫框架Scrapy， 人民邮电出版社
    ·[Python3网络爬虫](http://blog.csdn.net/c406495762/article/details/72858983)
    ·[Scrapy官方教程](http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html)
·前提知识
    ·url
    ·http协议
    ·web前端，html, css, js
    ·ajax
    ·re, xpath
    ·xml
# 1.爬虫简介
·爬虫定义：网络爬虫（又被称为网页蜘蛛，网络机器人，在FOAF社区中间，更经常的称为网页追逐者），是一种按照一定的规则，自动地抓取万维网信息的程序或者脚本。另外一些不常使用的名字还有蚂蚁、自动索引、模拟程序或者蠕虫。
·两大特征
    ·能按作者要求下载数据或者内容
    ·能自动在网络上流窜
·三大步骤：
    ·下载网页
    ·提取正确的信息
    ·根据一定规则自动跳到另外的网页上执行上两步内容   
·爬虫分类
    ·通用爬虫
    ·专用爬虫（聚焦爬虫）
·Python网络包简介
    ·Python2.x：urllib, urllib2, urllib3, httplib, httplib2, requests
    ·Python3.x: urllib, urllib3, httplib2, requests
    ·python2: urllib和urllib2配合使用，或者requests
    ·Python3： urllib，requests
# urllib
·包含模块
    ·urllib.request: 打开和读取urls
    ·urllib.error： 包含urllib.request产生的常见的错误，使用try捕捉
    ·urllib.parse:  包含解析url的方法
    ·urllib.robotparse: 解析robots.txt文件
    ·案例v1
    
·网页编码问题解决
    ·chardet 可以自动检测页面文件的编码格式，但是，可能有误
    ·需要安装，安装方法：在python的安装文件夹的scripts文件夹里面有个pip.exe文件，安装时需要用到这个(貌似python2.4版本以上才默认有这个功能)，在命令行模式下进入pip.exe所在的文件夹，然后在命令提示符中输入pip.exe install chardet
    ·Python获取网页编码的两种方法——requests.get、chardet
    ·案例v2
# urlopen 的返回对象（在例子中指的是rsp）
·返回对象具有的函数
    ·geturl: 返回请求对象的url
    ·info: 请求反馈对象的meta信息
    ·getcode：返回的http code    
    ·案例3（也可以在 print(type(rsp)) 一行打上断点，然后看编辑器下方Console中给出的信息，可以得到URL等信息）
# request.data 的使用
·访问网络的两种方法
    ·get: 
        ·利用参数给服务器传递信息，
        ·参数为dict，然后用parse编码 
        ·案例v4
    ·post
        ·一般向服务器传递参数使用
        ·post是把信息自动加密处理
        ·我们如果想使用psot信息，需要用到data参数
        ·使用post，意味着Http的请求头可能需要更改：
            ·Content-Type: application/x-www.form-urlencode
            ·Content-Length: 数据长度
            ·简而言之，一旦更改请求方法，请注意其他请求头部信息相适应
        ·urllib.parse.urlencode可以将字符串自动转换成上面的
        ·案例5
        ·为了更多的设置请求信息，单纯的通过urlopen函数已经不太好用了，需要利用request.Request 类
        ·案例6
# urllib.error
·（用 request.openurl() 都应该放在 try 中） 

·URLError产生的原因：
    ·没网
    ·服务器链接失败
    ·找不到指定服务器
    ·是OSError的子类
    ·案例7
·HTTPError, 是URLError的一个子类
    ·案例8
·两者区别：
    ·HTTPError是对应的HTTP请求的返回码错误, 如果返回错误码是400以上的，则引发HTTPError
    ·URLError对应的一般是网络出现问题，包括url问题
    ·关系区别： OSError-URLError-HTTPError
    ·最后值得注意的一点是，如果想用HTTPError和URLError一起捕获异常，那么需要将HTTPError放在URLError的前面，因为HTTPError是URLError的一个子类。如果URLError放在前面，出现HTTP异常会先响应URLError，这样HTTPError就捕获不到错误信息了。
    ·如果不用上面的方法，也可以使用hasattr函数判断URLError含有的属性，如果含有reason属性表明是URLError，如果含有code属性表明是HTTPError。案例9
# UserAgent（用户代理）
·有一些网站不喜欢被爬虫程序访问，所以会检测连接对象，如果是爬虫程序，也就是非人点击访问，它就会不让你继续访问，所以为了要让程序可以正常运行，需要隐藏自己的爬虫程序的身份。此时，我们就可以通过设置User Agent的来达到隐藏身份的目的，User Agent的中文名为用户代理，简称UA
·User Agent存放于Headers中，服务器就是通过查看Headers中的User Agent来判断是谁在访问。在Python中，如果不设置User Agent，程序将使用默认的参数，那么这个User Agent就会有Python的字样，如果服务器检查User Agent，那么没有设置User Agent的Python程序将无法正常访问网站
·Python允许我们修改这个User Agent来模拟浏览器访问
·UserAgent： 用户代理，简称UA， 属于heads的一部分，服务器通过UA来判断访问者身份
·常见的UA值，使用的时候可以直接复制粘贴，也可以用浏览器访问的时候抓包:     
    ·1.Android
        ·Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19
        ·Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
        ·Mozilla/5.0 (Linux; U; Android 2.2; en-gb; GT-P1000 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
    ·2.Firefox
        ·Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0
        ·Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0
    ·3.Google Chrome
        ·Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36
        ·Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19
    ·4.iOS
        ·Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3
        ·Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A101a Safari/419.3
·设置UA可以通过两种方式：
    ·在创建Request对象的时候，填入headers参数(包含User Agent信息)，这个Headers参数要求为字典
    ·在创建Request对象的时候不添加headers参数，在创建完成之后，使用add_header()的方法，添加headers
·案例10
# ProxyHandler（代理服务器）
·根据上面User Agent已经设置好了，但是还应该考虑一个问题，程序的运行速度是很快的，如果我们利用一个爬虫程序在网站爬取东西，一个固定IP的访问频率就会很高，这不符合人为操作的标准，因为人操作不可能在几ms内，进行如此频繁的访问。所以一些网站会设置一个IP访问频率的阈值，如果一个IP访问频率超过这个阈值，说明这个不是人在访问，而是一个爬虫程序。
·一个很简单的解决办法就是设置延时，但是这显然不符合爬虫快速爬取信息的目的，所以另一种更好的方法就是使用IP代理。
·ProxyHandler处理（代理服务器）
    ·使用代理IP，是爬虫的常用手段
    ·获取代理服务器的地址：（注意：当然也可以写个正则表达式从网站直接爬取IP，但是要记住不要太频繁爬取，加个延时什么的，太频繁给服务器带来压力了，服务器会直接把你block，不让你访问的。编写代码访http://www.whatismyip.com.tw/，该网站是测试自己IP为多少的网址，服务器会返回访问者的IP）
        ·www.xicidaili.com
        ·www.goubanjia.com
    ·代理用来隐藏真实访问中，代理也不允许频繁访问某一个固定网站，所以，代理一定要很多很多
    ·基本使用步骤：
        ·设置代理地址
        ·创建ProxyHandler：调用urlib.request.ProxyHandler()，proxies参数为一个字典
        ·创建Opener：opener = request.build_opener(proxy_handler)
        ·安装Opener：request.install_opener(opener)
·使用install_opener方法之后，会将程序默认的urlopen方法替换掉。也就是说，如果使用install_opener之后，在该文件中，再次调用urlopen会使用自己创建好的opener。如果不想替换掉，只是想临时使用一下，可以使用opener.open(url)，这样就不会对程序默认的urlopen有影响。
·案例11
# cookie & session
·为什么要使用Cookie
    ·Cookie，指某些网站为了辨别用户身份、进行session跟踪而储存在用户本地终端上的数据（通常经过加密)。 比如说有些网站需要登录后才能访问某个页面，在登录之前，你想抓取某个页面内容，登陆前与登陆后是不同的，或者不允许的。 使用Cookie和使用代理IP一样，也需要创建一个自己的opener。在HTTP包中，提供了cookiejar模块，用于提供对Cookie的支持。

·cookie & session
    ·由于http协议的无记忆性，人们为了弥补这个缺憾，所采用的一个补充协议
    ·cookie是发放给用户（即http浏览器）的一段信息，session是保存在服务器上的对应的另一半信息，用来记录用户信息，可以用F12查看Network中点击name中的信息然后可以查看cookie信息
·cookie和session的区别
    ·存放位置不同
    ·cookie不安全
    ·session会保存在服务器上一定时间，会过期
    ·单个cookie保存数据不超过4k， 很多浏览器限制一个站点最多保存20个
·session的存放位置
    ·存在服务器端
    ·一般情况，session是放在内存中或者数据库中
    ·没有cookie登录 ,可以看到，没使用cookie则反馈网页为未登录状态
    ·案例12 
·使用cookie登录
·http.cookiejar功能强大，我们可以利用本模块的CookieJar类的对象来捕获cookie并在后续连接请求时重新发送，比如可以实现模拟登录功能。该模块主要的对象有CookieJar、FileCookieJar、MozillaCookieJar、LWPCookieJar。
·（手动）直接把cookie复制下来，然后手动放入请求头
    ·案例 13
·（自动）http模块包含一些关于cookie的模块，通过他们我们可以自动使用cookie
    ·CookieJar
        ·管理存储cookie，向传出的http请求添加cookie，
        ·cookie存储在内存中，CookieJar实例回收后cookie将消失
    ·FileCookieJar(filename, delayload=None, policy=None):
        ·使用文件管理cookie
        ·filename是保存cookie的文件
    ·MozillaCookieJar(filename, delayload=None, policy=None):
        ·创建与mocilla浏览器cookie.txt兼容的FileCookieJar实例
    ·LwpCookieJar(filename, delayload=None, policy=None):
        ·创建与libwww-perl标准兼容的Set-Cookie3格式的FileCookieJar实例
    ·他们的关系是: CookieJar（派生出）-->FileCookieJar-->MozillaCookieJar & LwpCookieJar 
·工作原理：创建一个带有cookie的opener，在访问登录的URL时，将登录后的cookie保存下来，然后利用这个cookie来访问其他网址。查看登录之后才能看到的信息。
·利用cookiejar访问人人， 案例14
·自动使用cookie登录，大致流程是：
    ·打开登录页面后自动通过用户名密码登录
    ·自动提取反馈回来的cookie
    ·利用提取的cookie登录隐私页面 
·handler是Handler的实例，用来处理复杂请求，常用参看案例代码
    ·# 生成 cookie的管理器
    ·cookie_handler = request.HTTPCookieProcessor(cookie)
    ·# 创建http请求管理器
    ·http_handler = request.HTTPHandler()
    ·# 生成https管理器
    ·https_handler = request.HTTPSHandler()
·创立handler后，使用opener打开，打开后相应的业务由相应的hanlder处理 
·cookie作为一个变量，打印出来, 案例15
    ·cookie的属性
        ·name: 名称
        ·value： 值
        ·domain：可以访问此cookie的域名
        ·path： 可以访问此cookie的页面路径
        ·expires：过期时间
        ·size： 大小
        ·Http字段
·cookie的保存-FileCookieJar， 案例16
·cookie的读取， 案例17
# SSL
·SSL证书就是指遵守SSL安全套阶层协议的服务器数字证书（SercureSocketLayer)
·美国网景公司开发
·CA（CertifacateAuthority)是数字证书认证中心，是发放，管理，废除数字证书的收信人的第三方机构
·遇到不信任的SSL证书，（如 https://www.12306.cn , 360），需要单独处理
·案例18
# js加密
·有的反爬虫策略采用js对需要传输的数据进行加密处理（通常是取md5值)
·经过加密，传输的就是密文，但是
·加密函数或者过程一定是在浏览器完成，也就是一定会把代码（js代码）暴露给使用者
·通过阅读加密算法，就可以模拟出加密过程，从而达到破解
·过程参看案例19, 案例20
# ajax
·异步请求
·一定会有url，请求方法，可能有数据
·一般使用json格式
·案例21
# Requests-献给人类
·一、简介
    ·虽然Python的标准库中 urllib 模块已经包含了平常我们使用的大多数功能，但是它的 API 使用起来让人感觉不太好，而 Requests 自称 “HTTP for Humans”，更简洁更友好。
    ·Requests 唯一的一个非转基因的 Python HTTP 库，人类可以安全享用：）
    ·Requests 继承了urllib的所有特性。Requests支持HTTP连接保持和连接池，支持使用cookie保持会话，支持文件上传，支持自动确定响应内容的编码，支持国际化的 URL 和 POST 数据自动编码。
    ·requests 的底层实现其实就是 urllib3 。Requests能完全满足当前网络的需求，支持Python 2.6—3.5，而且能在PyPy下完美运行。
    ·开源地址：https://github.com/kennethreitz/requests或https://github.com/requests/requests
    ·中文文档 API：http://docs.python-requests.org/zh_CN/latest/index.html
    ·安装： conda install requests
·二、安装方式
    ·$ easy_install requests
    ·或
    ·$ conda install requests
    ·或
    ·$ pip install requests
·三、 GET请求
    ·1.requests.get(url)，案例22
    ·2.requests.request("get", url)，案例22
    ·3.可以带有headers和parmas参数，案例23。如果想添加 headers，可以传入headers参数来增加请求头中的headers信息。如果要将参数放在url中传递，可以利用params参数。
    ·4.get返回内容，案例23
·使用response.text 时，Requests 会基于 HTTP 响应的文本编码自动解码响应内容，大多数 Unicode 字符集都能被无缝地解码。
·使用response.content 时，返回的是服务器响应数据的原始二进制字节流，可以用来保存图片等二进制文件。

·四、POST请求
    ·最基本的GET请求可以直接用post方法 
    ·rsp = requests.post(url, data=data)
    ·传入data数据 
    ·对于 POST 请求来说，我们一般需要为它增加一些参数。那么最基本的传参方法可以利用data这个参数。
    ·date, headers要求dict类型，不需要转码了
    ·模拟有道翻译，案例24
·五、显示json文件
    ·# 自带json模块
    ·print(response.json())
·六、代理（proxies参数）
    ·如果需要使用代理，可以通过为任意请求方法提供proxies参数来配置单个请求(代理有可能报错，如果使用人数多，考虑安全问题，可能会被强行关闭)：
    ·案例25
·七、用户验证
    ·代理验证
        ·可能需要使用HTTP basic Auth， 可以这样
        ·格式为  用户名:密码@代理地址：端口地址
        ·proxy = { "http": "china:123456@192.168.1.123：4444"}
        ·rsp = requests.get("http://baidu.com", proxies=proxy)
    ·web客户端验证,如果遇到web客户端验证，需要添加auth=（用户名，密码）
    
            import requests
            auth = ("test1", "123456")  # 授权信息
            response = requests.get('http://192.168.199.107', auth=auth)
            print('response.text')
            import requests

·八、Cookies 和 Session
    ·1、Cookies
        ·requests可以自动处理cookie信息 
            
                    rsp = requests.get("http://xxxxxxxxxxxx")
                    # 如果对方服务器给传递过来cookie信息，则可以通过反馈的cookie属性得到
                    # 返回一个cookiejar实例
                    cookiejar = rsp.cookies
                    # 可以将cookiejar转换成字典
                    cookiedict = requests.utils.dict_from_cookiejar(cookiejar)   
                                
   ·2、Session
        ·跟服务器端session不是一个东东
        ·模拟一次会话，从客户端浏览器链接服务器开始，到客户端浏览器断开
        ·能让我们跨请求时保持某些参数，比如在同一个session实例发出的 所有请求之间保持cookie，以后所有请求都是这一个cookie，不需要再创建
            
                   # 创建session对象，可以保持cookie值
                   ss = requests.session()
                   
                   headers = {"User-Agetn":"xxxxxxxxxxxxxxxxxx"}
                   
                   data = {"name":"xxxxxxxxxxx"}
                          
                   此时，由创建的session管理请求，负责发出请求，
                   ss.post("http://www.baidu.com", data=data, headers=headers)
                           
                   rsp = ss.get("xxxxxxxxxxxx")

   ·在 requests 里，session对象是一个常用的对象，这个对象代表一次用户会话：从客户端浏览器连接服务器开始，到客户端浏览器与服务器断开。
   ·会话能让我们在跨请求时候保存某些参数，比如在同一个 Session 实例发出的所有请求之间保存cookie 。
   ·实现人人网登录：案例v26
·九、SSL证书验证
    ·https请求验证ssl证书(有一些网站的ssl证书是自己写的，比如12306和360)
    ·参数verify负责表示是否需要验证ssL证书，默认是True
    ·如果不需要验证ssl证书，则设置成False表示关闭
    
            rsp = requests.get("https://www.baidu.com", verify=False)
            # 如果用verify=True访问12306，会报错，因为他证书有问题 

   ·处理HTTPS请求 SSL证书验证 ,Requests也可以为HTTPS请求验证SSL证书：
   ·要想检查某个主机的SSL证书，你可以使用 verify 参数（也可以不写）
   
            import requests
            response = requests.get("https://www.baidu.com/", verify=True)
 
            # 也可以省略不写
            # response = requests.get("https://www.baidu.com/")
            print(response.text)
            
   ·如果SSL证书验证不通过，或者不信任服务器的安全证书，则会报出SSLError，据说 12306 证书是自己做的： 
   ·来测试一下： 
      
            import requests
            response = requests.get("https://www.12306.cn/mormhweb/")
            print(response.text)
            
   ·报错：
   
            SSLError: ("bad handshake: Error([('SSL routines', 
            'ssl3_get_server_certificate', 'certificate verify failed')],)",)
            
   ·如果我们想跳过 12306 的证书验证，把 verify 设置为 False 就可以正常请求了。         

            import requests
 
            url = "https://www.12306.cn/mormhweb/"
            response = requests.get(url,verify=False)
            print(response.text)


