# HTTP协议
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
