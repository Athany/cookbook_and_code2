# HTTP协议
·https://blog.51cto.com/13570193/2108347
## HTTP简介
·超文本(HyperText)：包含有链接(Link)和各种多媒体元素标记(Markup)的文本。这些超文本文件彼此链接，形成网状(Web),因此又被称为网页(Web Page)。这些链接使用URL表示。最常见的超文本是超文本标记语言HTML。
·URL：即统一资源定位符(Uniform Resource Locator)，用来唯一地标识万维网中的某一个文档。URL由协议。主机和端口(默认为80)以及文件名三部分组成。如：http://(协议://)www.sxtyu.xom:80(主机:端口(80)/)/news/index.html(文件名及其路径)
·HTTP：是一种按照URL指示，将超文本文档从一台主机(Web服务器)传输到另一台主机(浏览器)的应用层协议，以实现超链接的功能。
    ·在用户点击URL为 http://www.sxtyu.com/index.html 的链接后,浏览器好Web服务器执行以下动作：
        ·1.浏览器分析超链接中的URL
        ·2.浏览器向DNS请求解析 www.sxtyu.com 的IP地址
        ·3.DNS将解析出的IP地址202.2.16.21返回浏览器
        ·4.浏览器与服务器建立TCP连接(80端口)
        ·5.浏览器请求文档：GET/index.html
        ·6.服务器给出响应，将文档index.html发送给浏览器
        ·7.释放TCP连接
        ·8.浏览器显示index.html中的内容
    ·非持久连接
        ·即浏览器每请求一个Web文档，就创建一个新的连接，当文档传输完毕后 ，连接就立刻被释放。
        ·HTTP1.0、HTTP0.9采用此连接
        ·对于请求的Web页中包含多个其他文档对象(如图像、声音、视频等)的链接的情况，由于请求每个链接对应的文档都要创建新链接，效率低下。
    ·持久连接
        ·即在一个链接中，可以进行多次文档的请求和响应。服务器在发送响应后，并不立即释放连接，浏览器可以使用该连接继续请求其他文档。连接保持的时间可以由双方进行协商。
    ·无状态性
        ·是指同一个客户端(浏览器)第二次访问同一个Web服务器上的页面时，服务器无法知道这个客户曾经访问过。HTTP的无状态性简化了服务器的设计，使其更容易支持大量并发的HTTP请求。
## HTTP报文结构
### 请求报文
·即从客户端(浏览器)向Web服务器发送的请求报文。报文的所有字段都是ASCII码。
### 返回报文
·即从Web服务器到客户端(浏览器)的应答。报文的所有字段都是ASCII码。
### 请求报文中的方法
·方法(Method)是对所有请求对象所进行的操作，也就是一些命令。请求报文中的所有操作有：
    ·GET：请求读取一个Web页面
    ·POST：附加一个命名资源(如Web页面)
    ·DELETE：删除Web页面
    ·CONNECT：用于代理服务器
    ·HEAD：请求读取一个Web页面的首部
    ·PUT：请求存储一个Web页面
    ·TRACE：用于测试，要求服务器送回收到的请求
    ·OPTION：查询特定选项
### 响应报文中的状态码
### 状态码(Status-Code)是响应报文状态行中包含的一个3位数字，指明特定的请求是否被满足，如果没有满足，原因是什么。状态码分为以下五类：  
            状态码	 含义	         例子
            1xx	 通知信息	     100=服务器正在处理客户请求
            2xx	 成功	         200=请求成功(OK)
            3xx	 重定向	     301=页面改变了位置
            4xx	 客户错误	     403=禁止的页面；404=页面未找到
            5xx	 服务器错误	 500=服务器内部错误；503=以后再试
·具体各状态码的含义，请参考W3C的HTTP1.1标准规范RFC2616  http://www.w3.org/Protocols/rfc2616/rfc2616.html
### 首部字段或消息头
            头（header）	     类型	        说明
            User-Agent	         请求	        关于浏览器和它平台的信息，如Mozilla5.0
            Accept	             请求	        客户能处理的页面的类型，如text/html
            Accept-Charset	     请求	        客户可以接受的字符集，如Unicode-1-1
            Accept-Encoding	 请求	        客户能处理的页面编码方法，如gzip
            Accept-Language	 请求	        客户能处理的自然语言，如en(英语)、zh-cn(简体中文)
            Host	             请求	        服务器的DNS名称。从URL中提取处理，必需。
            Authorization	     请求	        客户的信息凭据列表
            Cookie	             请求	        将以前设置的Cookie送回服务器，可用来作为会话信息
            Date	             双向	        消息被发送时的日期和时间
            Server	             响应	        关于服务器的信息，如Microsoft-IIS/6.0
            Content-Encoding	 响应	        内容是如何被编码的(gzip)
            Content-Language	 响应	        页面所使用的自然语言
            Content-Length	     响应	        以字节计算的字节长度
            Content-Type	     响应	        页面的MIME类型
            Last-Modified	     响应	        页面最后被修改的时间和日期，在页面缓存机制中意义重大
            Location	         响应	        指示客户将请求发送给别处，即重定向到另一个URL
            Set-Cookie	         响应	        服务器希望客户保存一个Cookie
### 报文结构实例
·请求 www.baidu.com 时的返回头文件
·General
    ·Request URL: https://www.baidu.com/
    ·Request Method: GET
    ·Status Code: 200 OK
    ·Remote Address: 119.75.213.61:443
    ·Referrer Policy: no-referrer-when-downgrade
·Response Header
    ·HTTP/1.1 200 OK
    ·Bdpagetype: 1
    ·Bdqid: 0x9085388700019bf7
    ·Cache-Control: private
    ·Connection: Keep-Alive
    ·Content-Encoding: gzip
    ·Content-Type: text/html
    ·Cxy_all: baidu+1ec559cf68a7aa4a3686deb9339c619a
    ·Date: Sun, 15 Jul 2018 08:33:37 GMT
    ·Expires: Sun, 15 Jul 2018 08:32:50 GMT
    ·Server: BWS/1.1
    ·Set-Cookie: BDSVRTM=0; path=/
    ·Set-Cookie: BD_HOME=0; path=/
    ·Set-Cookie: H_PS_PSSID=1455_26433_21096_18559_26350_20930; path=/; domain=.baidu.com
    ·Strict-Transport-Security: max-age=172800
    ·Vary: Accept-Encoding
    ·X-Ua-Compatible: IE=Edge,chrome=1
    ·Transfer-Encoding: chunked
·Request Header
    ·Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8
    ·Accept-Encoding: gzip, deflate, br
    ·Accept-Language: zh-CN,zh;q=0.9
    ·Cache-Control: no-cache
    ·Connection: keep-alive
    ·Cookie: BAIDUID=01316B4CFA260ABC4134B0E2EAAE5AE9:FG=1; BIDUPSID=01316B4CFA260ABC4134B0E2EAAE5AE9; PSTM=1513852327; __cfduid=d0deb43cfccca6142401388cc3908eea61521620771; MCITY=-%3A; sug=3; sugstore=0; ORIGIN=2; bdime=0; BD_UPN=12314353; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSFRCVID=ppKsJeCCxG3wW0b7siHpjnd3NiUdQvfiKQYI3J; H_BDCLCKID_SF=tRk8oKPyJKvhKROmK4r2q4tehHRjbUneWDTm5-nTt-3Rhb_6KPr1K-IHbabwalQbL6chBlvlylI5OCcnK4-XD6Q0eHQP; BD_CK_SAM=1; PSINO=1; H_PS_PSSID=1455_26433_21096_18559_26350_20930; H_PS_645EC=678dd2FJdRJMzCOvLAajSA3Iy17n1MpCniMhU4IxIp5uJ7oShBuWJBfMsIs; BD_HOME=0
    ·Host: www.baidu.com
    ·Pragma: no-cache
    ·Upgrade-Insecure-Requests: 1
    ·User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36
### HTTP 代理
### 什么是HTTP代理
·HTTP代理又称Web缓存或代理服务器(Proxy Server)，是一种网络实体，能代表浏览器发出HTTP请求，并将最近的一些请求和响应暂存在本地磁盘中，当请求的Web页面先前暂存过，则直接将暂存的页面发给客户端(浏览器)，无法再次访问Internet。
### 使用HTTP代理的Web访问过程
·浏览器向HTTP代理发出页面请求---->HTTP代理查找缓存页面--找到-->用缓存页面响应请求
·浏览器向HTTP代理发出页面请求---->HTTP代理查找缓存页面--未找到-->代表浏览器向源Web服务器发出请求---->源Web服务器响应HTTP代理---->HTTP代理缓存请求到的页面---->将请求到的页面响应给浏览器







https://blog.51cto.com/13570193/2108347
HTTP--Hyper Text Transfer Protocol，超文本传输协议，是一种建立在TCP上的无状态连接，整个基本的工作流程是客户端发送一个HTTP请求，说明客户端想要访问的资源和请求的动作，服务端收到请求之后，服务端开始处理请求，并根据请求做出相应的动作访问服务器资源，最后通过发送HTTP响应把结果返回给客户端。其中一个请求的开始到一个响应的结束称为事务，当一个事物结束后还会在服务端添加一条日志条目。

目录

HTTP请求

HTTP响应

HTTP报文格式

HTTP协议版本更替

网站访问量

一、HTTP请求

        HTTP请求是客户端往服务端发送请求动作，告知服务器自己的要求。

        HTTP请求由状态行、请求头、请求正文三部分组成：

状态行：包括请求方式Method、资源路径URL、协议版本Version；

请求头：包括一些访问的域名、用户代理、Cookie等信息；

请求正文：就是HTTP请求的数据。

        备注：请求方式Method一般有GET、POST、PUT、DELETE，含义分别是获取、修改、上传、删除，其中GET方式仅仅为获取服务器资源，方式较为简单，因此在请求方式为GET的HTTP请求数据中，请求正文部分可以省略，直接将想要获取的资源添加到URL中。下图所示就是GET的请求，没有请求正文。详细的说明在下边。

        现在大多数协议版本为http/1.1

blob.png

        下图所示为POST请求的格式，有状态行、请求头、请求正文三部分。

blob.png


二、HTTP响应

2.1 响应数据格式

        服务器收到了客户端发来的HTTP请求后，根据HTTP请求中的动作要求，服务端做出具体的动作，将结果回应给客户端，称为HTTP响应。

        HTTP响应由三部分组成：状态行、响应头、响应正文；

状态行：包括协议版本Version、状态码Status Code、回应短语；

响应头：包括搭建服务器的软件，发送响应的时间，回应数据的格式等信息；

响应正文：就是响应的具体数据。

        备注：我们主要关心并且能够在客户端浏览器看得到的是三位数的状态码，不同的状态码代表不同的含义，其中


1xx	表示HTTP请求已经接受，继续处理请求
2xx	表示HTTP请求已经处理完成
3xx	表示把请求访问的URL重定向到其他目录
4xx	表示客户端出现错误
5xx	表示服务端出现错误
具体HTTP响应实例如下图：

blob.png

2.2 常见状态码的含义

        200---OK/请求已经正常处理完毕

        301---/请求永久重定向

        302---/请求临时重定向

        304---/请求被重定向到客户端本地缓存

        400---/客户端请求存在语法错误

        401---/客户端请求没有经过授权

        403---/客户端的请求被服务器拒绝，一般为客户端没有访问权限

        404---/客户端请求的URL在服务端不存在

        500---/服务端永久错误

        503---/服务端发生临时错误

2.3 HTTP响应模型

        服务器收到HTTP请求之后，会有多种方法响应这个请求，下面是HTTP响应的四种模型：

        单进程I/O模型

服务端开启一个进程，一个进程仅能处理一个请求，并且对请求顺序处理；

        多进程I/O模型

服务端并行开启多个进程，同样的一个进程只能处理一个请求，这样服务端就可以同时处理多个请求；

        复用I/O模型

服务端开启一个进程，但是呢，同时开启多个线程，一个线程响应一个请求，同样可以达到同时处理多个请求，线程间并发执行；

        复用多线程I/O模型

服务端并行开启多个进程，同时每个进程开启多个线程，这样服务端可以同时处理进程数M*每个进程的线程数N个请求。

三、HTTP报文格式

        HTTP报文是HTTP应用程序之间传输的数据块，HTTP报文分为HTTP请求报文和HTTP响应报文，但是无论哪种报文，他的整体格式是类似的，大致都是由起始、首部、主体三部分组成，起始说明报文的动作，首部说明报文的属性，主体则是报文的数据。接下来具体说明。

3.1 HTTP请求报文

blob.png      

        请求报文的起始由请求行构成（有些资料称为状态行，名字不一样而已，都是指的一个东西），用来说明该请求想要做什么，由<Method>、<URL>、<Version> 三个字段组成，注意每个字段之间都有一个空格。

        其中<Method>字段有不同的值：

                GET   --- 访问服务器的资源

                POST  --- 向服务器发送要修改的数据

                HEAD  --- 获取服务器文档的首部

                PUT   --- 向服务器上传资源

                DELETE--- 删除服务器的资源

        <URL>字段表示服务器的资源目录定位

        <Version>字段表示使用的http协议版本

        首部部分由多个请求头（也叫首部行）构成，那些首部字段名有如下，不全：

                Accept     指定客户端能够接收的内容格式类型

                Accept-Language 指定客户端能够接受的语言类型

                Accept-Ecoding  指定客户端能够接受的编码类型

                User-Agent      用户代理，向服务器说明自己的操作系统、浏览器等信息

                Connection      是否开启持久连接（keepalive）

                Host            服务器域名

                ...

        主体部分就是报文的具体数据。                      

3.2 HTTP响应报文

blob.png     

        响应报文的起始由状态行构成，用来说明服务器做了什么，由<Version>、<Status-Code>、<Phrase>三个字段组成，同样的每个字段之间留有空格；

        <Status-Code> 上边已经说明； 

        首部由多个响应头(也叫首部行)组成， 首部字段名如下，不全：

                Server    服务器软件名，Apache/Nginx

                Date      服务器发出响应报文的时间

                Last-Modified   请求资源的最后的修改时间

                ...

        主体部分是响应报文的具体数据。

小tips：关于更多请求头和响应头（即首部字段名）的说明请参考http://tools.jb51.net/table/http_header   


四、HTTP协议版本更替

HTTP/0.9

        HTTP协议的最初版本，功能简陋，仅支持请求方式GET，并且仅能请求访问HTML格式的资源。

HTTP/1.0    

        在0.9版本上做了进步，增加了请求方式POST和HEAD；不再局限于0.9版本的HTML格式，根据Content-Type可以支持多种数据格式，即MIME多用途互联网邮件扩展，例如text/html、image/jpeg等；同时也开始支持cache，就是当客户端在规定时间内访问统一网站，直接访问cache即可。

        但是1.0版本的工作方式是每次TCP连接只能发送一个请求，当服务器响应后就会关闭这次连接，下一个请求需要再次建立TCP连接，就是不支持keepalive。

HTTP/1.1    

        解决了1.0版本的keepalive问题，1.1版本加入了持久连接，一个TCP连接可以允许多个HTTP请求； 加入了管道机制，一个TCP连接同时允许多个请求同时发送，增加了并发性；新增了请求方式PUT、PATCH、DELETE等。

        但是还存在一些问题，服务端是按队列顺序处理请求的，假如一个请求处理时间很长，则会导致后边的请求无法处理，这样就造成了队头阻塞的问题；同时HTTP是无状态的连接，因此每次请求都需要添加重复的字段，降低了带宽的利用率。

HTTP/2.0

        为了解决1.1版本利用率不高的问题，提出了HTTP/2.0版本。增加双工模式，即不仅客户端能够同时发送多个请求，服务端也能同时处理多个请求，解决了队头堵塞的问题；HTTP请求和响应中，状态行和请求/响应头都是些信息字段，并没有真正的数据，因此在2.0版本中将所有的信息字段建立一张表，为表中的每个字段建立索引，客户端和服务端共同使用这个表，他们之间就以索引号来表示信息字段，这样就避免了1.0旧版本的重复繁琐的字段，并以压缩的方式传输，提高利用率。

        另外也增加服务器推送的功能，即不经请求服务端主动向客户端发送数据。

当前主流的协议版本还是HTTP/1.1版本。

五、网站访问量


        IP IP访问量

相同的公网IP计算一次，就是同一个局域网内的所有用户访问一个网站，但是他们都是借助一个公网IP去访问那个网站的（NAT），因此这也只能算作一个IP访问量。换一次公网IP则会加1。

        PV 网页访问量

用户访问的页面数就是PV访问量，同一个局域网的不同用户，而且就算是同一个用户，只要刷新一次网站页面，PV访问量就加1，三个访问量的值往往数PV的值最大。

        UV 访客访问量

这里的访客不是用户，而是电脑，一台电脑算一个访客，即使是同一台电脑的不同用户，访问同一个网站UV也只能加1，只有更换电脑才会使UV加1，因为服务端会记录客户端电脑的信息