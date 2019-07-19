# 页面解析和数据提取
·一般来讲对我们而言，需要抓取的是某个网站或者某个应用的内容，提取有用的价值。内容一般分为两部分，非结构化的数据和 结构化的数据。
·非结构化数据：先有数据，再有结构，
·结构化数据：先有结构、再有数据
·不同类型的数据，我需要采用不同的方式来处理。

·非结构化的数据处理
    ·文本、电话号码、邮箱地址：
        ·正则表达式
    ·html文件：
        ·正则表达式
        ·xpath
        ·css选择器
        ·bs4 
·结构化的数据处理
    ·json文件：
        ·jsonPath
        ·转化成Python类型进行操作（json类）
    ·xml文件：
        ·转化成Python类型（xmltodict）
        ·XPath
        ·CSS选择器
        ·正则表达式 
# CSS选择器  Beautiful Soup 4.2.0 文档
·更为详细内容，可参考官方文档，URL：http://beautifulsoup.readthedocs.io/zh_CN/latest/ 
·一、简介
    ·官方文档：http://beautifulsoup.readthedocs.io/zh_CN/v4.4.0
    ·https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
    ·Beautiful Soup是一个HTML / XML的解析器，主要的功能是解析和提取HTML / XML数据。
        ·lxml只会局部遍历，而Beautiful Soup是基于HTML DOM的，会载入整个文档，解析整个DOM树，因此时间和内存开销都会大很多，所以性能要低于lxml。
        ·BeautifulSoup用来解析HTML比较简单，API非常人性化，支持CSS选择器，Python标准库中的HTML解析器，也支持lxml的XML解析器。
        ·Beautiful Soup 3目前已经停止开发，推荐现在的项目使用Beautiful Soup 4.使用pip安装即可：pip install beautifulsoup4

        ·抓取工具	          速度	使用难度	安装难度
        ·正则	              最快	困难	    无（内置）
        ·BeautifulSoup	      慢	最简单   	简单
        ·LXML	              快	简单  	    一般
        
   ·案例v39
·二、bs4的使用 
    ·1、导入模块
        ·#安装 Beautiful Soup
        ·pip install html5lib
        ·#安装解析器
        ·pip install lxml 
    ·2、获取节点
        ·案例v27
    ·3、寻找节点
        ·3.1 通过find()来查找
        ·案例v28
        3.2通过find_all()来查找
        ·案例v29
        3.3 通过select()来查找
        ·案例v30
·四大对象
    ·Tag
    ·NavigableString
    ·BeautifulSoup
    ·Comment
·Tag
    ·对应Html中的标签
    ·可以通过soup.tag_name
    ·tag两个重要属性
        ·name
        ·attrs
    ·案例v40
·NavigableString
    ·对应内容值,按照字面意义上理解为可遍历字符串，soup.tag.string 用来获取便签内部的文字内容，通过.string来调用
·BeautifulSoup
    ·表示一个文档的内容，大部分可以把它当做tag对象
    ·一般我们可以用soup来表示
·Comment
    ·特殊类型的NavigableString对象
    ·对其输出，则内容不包括注释符号
    
·遍历文档对象
    ·contents ：tag的子节点以列表的方式给出
    ·children ：子节点以迭代器形式返回
    ·descendants ：所以子孙节点
    案例v41
·搜索文档对象
    ·find_all(name, attrs, recursive, text, **kwargs)
        ·name 参数：可以查找所有名字为 name 的tag,字符串对象会被自动忽略掉
            ·A.传字符串
                ·最简单的过滤器是字符串.在搜索方法中传入一个字符串参数,Beautiful Soup会查找与字符串完整匹配的内容,下面的例子用于查找文档中所有的<b>标签。
                    soup.find_all('b')
                    # [<b>The Dormouse's story</b>] 
                    print soup.find_all('a')
                    #[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]            
            ·B.传正则表达式
                ·如果传入正则表达式作为参数,Beautiful Soup会通过正则表达式的 match() 来匹配内容.下面例子中找出所有以b开头的标签,这表示<body>和<b>标签都应该被找到。
                    import re
                    for tag in soup.find_all(re.compile("^b")):
                        print(tag.name)
                    # body
                    # b
            ·C.传列表
                ·如果传入列表参数,Beautiful Soup会将与列表中任一元素匹配的内容返回.下面代码找到文档中所有<a>标签和<b>标签    
                    soup.find_all(["a", "b"])
                    # [<b>The Dormouse's story</b>,
                    #  <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
                    #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
                    #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
        ·keyword 参数 
            soup.find_all(id='link2')
            # [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
        ·text 参数
            ·通过 text 参数可以搜搜文档中的字符串内容，与 name 参数的可选值一样, text 参数接受 字符串 , 正则表达式 , 列表
                soup.find_all(text="Elsie")
                # [u'Elsie']
                soup.find_all(text=["Tillie", "Elsie", "Lacie"])
                # [u'Elsie', u'Lacie', u'Tillie']
                soup.find_all(text=re.compile("Dormouse"))
                [u"The Dormouse's story", u"The Dormouse's story"]
·CSS选择器
·这就是另一种与 find_all 方法有异曲同工之妙的查找方法.
·写 CSS 时，标签名不加任何修饰，类名前加.，id名前加#
·在这里我们也可以利用类似的方法来筛选元素，用到的方法是 soup.select()，返回类型是 list
·（1）通过标签名查找                
        print soup.select('title') 
        #[<title>The Dormouse's story</title>]
        print soup.select('a')
        #[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
        print soup.select('b')
        #[<b>The Dormouse's story</b>]
·（2）通过类名查找
        print soup.select('.sister')
        #[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
·（3）通过 id 名查找
        print soup.select('#link1')
        #[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]
·（4）组合查找
·组合查找即和写 class 文件时，标签名与类名、id名进行的组合原理是一样的，例如查找 p 标签中，id 等于 link1的内容，二者需要用空格分开      
        print soup.select('p #link1')
        #[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]
·直接子标签查找，则使用 > 分隔 
        print soup.select("head > title")
        #[<title>The Dormouse's story</title>]
·（5）属性查找
·查找时还可以加入属性元素，属性需要用中括号括起来，注意属性和标签属于同一节点，所以中间不能加空格，否则会无法匹配到。
        print soup.select('a[class="sister"]')
        #[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>] 
        print soup.select('a[href="http://example.com/elsie"]')
        #[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]
·同样，属性仍然可以与上述查找方式组合，不在同一节点的空格隔开，同一节点的不加空格
        print soup.select('p a[href="http://example.com/elsie"]')
        #[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]
·（6）获取内容
以上的 select 方法返回的结果都是列表形式，可以遍历形式输出，然后用 get_text() 方法来获取它的内容。        
         soup = BeautifulSoup(html, 'lxml')
         print type(soup.select('title'))
         print soup.select('title')[0].get_text()
         for title in soup.select('title'):
             print title.get_text()
·案例v42
        
        
# 正则表达式
·一套规则，可以在字符串文本中进行搜查替换等
·https://baike.baidu.com/item/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F/1700215?fr=aladdin
·w3cschool教程：https://www.w3cschool.cn/zhengzebiaodashi/regexp-tutorial.html
·新w3cschool教程：http://www.hechaku.com/p/zhengze/
·菜鸟教程：http://www.runoob.com/python/python-reg-expressions.html

·案例v31,re的基本使用流程
·案例v32，match的基本使用
·正则常用方法：
    ·match: 从开始位置开始查找，一次匹配,找到一个就结束
    ·search：从任何位置查找，一次匹配， 案例v33
    ·findall： 全部匹配，返回列表, 案例v34
    ·finditer： 全部匹配，返回迭代器, 案例v34
    ·split： 分割字符串，返回列表
    ·sub：替换
·匹配中文
    ·中文unicode范围主要在[u4e00-u9fa5]
    ·案例v35
·贪婪与非贪婪模式
    ·贪婪模式： 在整个表达式匹配成功的前提下，尽可能多的匹配
    ·非贪婪模式： xxxxxxxxxxxxxxxxxxxxxx, 尽可能少的匹配
    ·python里面数量词默认是贪婪模式
    ·例如：
        ·查找文本abbbbbbccc
        ·re是 ab*
        ·贪婪模式： 结果是abbbbbb
        ·非贪婪： 结果是a 

# XML
·XML(EXtensibleMarkupLanguage)   
·学习文档：  http://www.w3school.com.cn/xml/index.asp
·案例v36
·概念：父节点，子节点，先辈节点，兄弟节点，后代节点
# XPath（python爬虫使用XPath解析页面和提取数据）
·一、简介
    ·XPath即为XML路径语言，它是一种用来确定XML（标准通用标记语言的子集）文档中某部分位置的语言。XPath基于XML的树状结构，有不同类型的节点，包括元素节点，属性节点和文本节点，提供在数据结构树中找寻节点的能力。
·二、什么是 XPath?
    ·XPath(XML Path Language), 是一门在XML文档中查找信息的语言 
    ·XPath 使用路径表达式在 XML 文档中进行导航
    ·XPath 包含一个标准函数库
    ·XPath 是 XSLT 中的主要元素
    ·XPath 是一个 W3C 标准
    ·官方文档： http://www.w3school.com.cn/xpath/index.asp
    ·XPath开发工具：
        ·开源的XPath表达式工具： XMLQuire
        ·chrome插件： Xpath Helper
        ·Firefox插件： XPath CHecker
·三、使用xpath
    ·1、导入模块
#首先安装库 pip install lxml

        import lxml
        from lxml import etree
        
   ·2、XPath Helper插件
        ·chrome插件网：http://www.cnplugins.com/
        ·GitHub下载:https://github.com/liangdongchang/tools
        ·在谷歌浏览器添中加插件
        ·Ctrl + Shift + X打开或关闭插件
   ·3、XPath 术语
        ·节点（Node）
        ·在 XPath 中，有七种类型的节点：元素、属性、文本、命名空间、处理指令、注释以及文档（根）节点。XML 文档是被作为节点树来对待的。树的根被称为文档节点或者根节点。
        ·基本值（或称原子值，Atomic value）
        ·基本值是无父或无子的节点。
        ·项目（Item）
        ·项目是基本值或者节点。
        ·节点关系
        ·父（Parent）
        ·每个元素以及属性都有一个父。
        ·子（Children）
        ·元素节点可有零个、一个或多个子。
        ·同胞（Sibling）
        ·拥有相同的父的节点
        ·先辈（Ancestor）
        ·某节点的父、父的父，等等。
        ·后代（Descendant）
        ·某个节点的子，子的子，等等
   ·4、选取节点
        ·XPath 使用路径表达式在 XML 文档中选取节点。节点是通过沿着路径或者 step 来选取的。 下面列出了最有用的路径表达式：

                表达式	     描述
                /            从根节点选取。
                //	         从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。
                .	         选取当前节点。
                ..	         选取当前节点的父节点。
                @	         选取属性。
                nodename	选取此节点的所有子节点


                路径表达式	                  结果
                bookstore	                  选取 bookstore 元素的所有子节点。
                /bookstore	                  选取根元素 bookstore。注释：假如路径起始于正斜杠( / )，则此路径始终代表到某元素的绝对路径！
                /bookstore/book	              选取属于 bookstore 的子元素的所有 book 元素。
                //book	                      选取所有 book 子元素，而不管它们在文档中的位置。
                bookstore//book	              选择属于 bookstore 元素的后代的所有 book 元素，而不管它们位于 bookstore 之下的什么位置。
                //@lang	                      选取名为 lang 的所有属性。
   5、 谓语（Predicates）
        ·谓语用来查找某个特定的节点，被镶嵌在方括号中或者包含某个指定的值的节点。在下面的表格中，我们列出了带有谓语的一些路径表达式，以及表达式的结果：
        
        路径表达式	结果
        /bookstore/book[1]	              选取属于 bookstore 子元素的第一个 book 元素。
        /bookstore/book[last()]	          选取属于 bookstore 子元素的最后一个 book 元素。
        /bookstore/book[last()-1]	      选取属于 bookstore 子元素的倒数第二个 book 元素。
        /bookstore/book[position()<3]	  选取最前面的两个属于 bookstore 元素的子元素的 book 元素。
        //title[@lang]	                  选取所有拥有名为 lang 的属性的 title 元素。
        //title[@lang=’cn’]	          选取属于bookstore下叫book的,含有属性lang的值是cn的元素。
        /bookstore/book[price<90]	      选取属于bookstore下叫book的,含有属性price的，且值小于90的元素。
        /bookstore/book[price<90]/title	  选取属于bookstore下叫book的,含有属性price的，且值小于90的元素的子元素title。
   6、通配符（选取未知节点）
        ·XPath 通配符可用来选取未知的 XML 元素。
        
            通配符	                  描述
            *	                      匹配任何元素节点。
            @*	                      匹配任何属性节点。
            node()	                  匹配任何类型的节点。
 `    ·在下面的表格中，我们列出了一些路径表达式，以及这些表达式的结果：

            路径表达式	                   结果
            /bookstore/*	               选取 bookstore 元素的所有子元素。
            //*	                           选取文档中的所有元素。
            //title[@*]	                   选取所有带有属性的 title 元素。
   ·7、选取多个路径
        ·通过在路径表达式中使用”|”运算符，您可以选取若干个路径。
        ·在下面的表格中，我们列出了一些路径表达式，以及这些表达式的结果：
        
            路径表达式	                            结果
            //book/title | //book/author	        选取 book 元素的所有 title 和 author元素。
            //title | //price	                    选取文档中的所有 title 和 price 元素。
            /bookstore/book/title | //price	        选取属于 bookstore 元素的 book 元素的所有 title 元素，以及文档中所有的 price 元素。
   ·8、XPath 实例 
        ·案例v37 
# etree和XPath实战
·案例v38

