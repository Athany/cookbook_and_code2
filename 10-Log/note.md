# LOG 日志
·logging
·logging模块提供模块级别的函数记录日志
·包括四大组件

# 日志相关概念
·日志
·日志的级别(level)
　　·不同的用户关注不同的程序信息
　　·DEBUG
　　·INFO
　　·NOTICE
　　·WARNING
　　·ERROR
　　·CRITICAL
　　·ALERT
　　·EMERGENCT
·IO操作不要太频繁
·LOG的作用
　　·调试
　　·了解软件的运行情况
　　·分析定位问题
·日志的信息
　　·time
　　·地点
　　·level
　　·内容
·成熟的第三方日志
　　·log4j
　　·log4php
　　·logging

 

# 2.logging模块	
·日志级别
　　·级别可自定义
　　·DEBUG
　　·INFO
　　·WARNING
　　·ERROR
　　·CRITICAL
·初始化/写日志实例需要指定级别，只有当级别等于或高于指定级别才被记录
·使用方式
　　·直接使用logging(封装了其他组件)
　　·logging四大组件直接定制
# 2.1 logging模块级别的日志
·使用以下几个函数
　　·logging.debug(msg,*args,**kwargs)创建一条严重级别为DEBUG的日志记录
　　·logging.info(msg,*args,**kwargs)创建一条严重级别为INFO的日志记录
　　·logging.warning(msg,*args,**kwargs)创建一条严重级别为WARNING的日志记录
　　·logging.error(msg,*args,**kwargs)创建一条严重级别为ERROR的日志记录
　　·logging.critical(msg,*args,**kwargs)创建一条严重级别为CRITICAL的日志记录
　　·logging.log(level,*args,**kwargs)创建一条严重级别为LEVEL的日志记录
　　·logging.basicConfig(**kwargs) 对root logger进行一次性配置
               # alt加左键选择多行同时操作
·logging.basicConfig(**kwargs) 对root logger进行一次性配置
　　·只在第一次调用的时候起作用
　　·不配置logger则使用默认值
　　　　·输出：sys.stderr
　　　　·级别：WARNING
　　　　·格式：level:log_name:content（级别：日志名称：内容）

# 案例-1	
import logging	
logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")
此时只会显示高于warning级别的日志

 

# 定制日志
import logging	
# 定义日志的生成时间及日志的格式
LOG_FORMAT = "%(asctime)s....%(levelname)s....%(massage)s"
# 显示所有级别的日志
logging.basicConfig(filename="zz.log",level=logging.DEBUG,format=LOG_FORMAT)

logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log."
此时可以显示以上所有日志，还可以加上日志生成的目录，以及定义日志的书写格式

# 有用的format格式
       格式	       描述
    %(levelno)s	    打印日志级别的数值
    %(levelname)s	打印日志级别名称
    %(pathname)s	打印当前执行程序的路径
    %(filename)s	打印当前执行程序名称
    %(funcName)s	打印日志的当前函数
    %(lineno)d	    打印日志的当前行号
    %(asctime)s	    打印日志的时间
    %(thread)d	    打印线程id
    %(threadName)s	打印线程名称
    %(process)d	    打印进程ID
    %(message)s	    打印日志信息

# 2.1 logging模块的处理流程
·四大组件
　　·日志器（Logger）：产生日志的一个接口
　　·处理器(Handler)：把产生的日志发送到相应的目的地
　　·过滤器(Filter): 更精细地控制日志输出
　　·格式器(Formatter)：对输出的信息进行格式化
·Logger
　　·产生一个日志
　　·操作
　　　　·Logger.setLevel()：设置日志器将会处理的日志消息的最低严重级别
　　　　·Logger.addHandler()和Logger.removeHandler()：为logger添加或移除对象
　　　　·Logger.addFilter()和Logger.removeFilter()：为logger添加或移除对象
　　　　·Logger.debug:产生一条debug级别的日志，同理得到info/error等
　　　　·Logger.exception():创建类似于Logger.error的日志消息
　　　　·Logger.log():获取一个明确的日志level参数类创建一个日志记录
　　·如何得到一个logger对象
　　　　·实例化
　　　　·logging.getLogger()

·Handler	
　　·把log发送到指定位置
　　·方法
　　　　·setLevel
　　　　·setFormat
　　　　·addFilter , removeFilter
　　·不需要直接使用，Handler是基类	
　　　　logging.StreamHandler ：将日志发送到输出到Stream，如stu.out，std.err或任何file-like对象
　　　　logging.FilterHandler ：将日志消息发送到磁盘文件，默认情况下文件大小无限增长
　　　　logging.handlers.RotatingFileHandler ：将日志消息发送到磁盘文件，并支持日志文件按大小切割
　　　　logging.handlers.TimeRotatingFileHandler ：将日志消息发送到磁盘文件，并支持日志文件按时间切割
　　　　logging.handlers.HTTPHandler ：将日志消息以GET或POST的方式发送给一个HTTP服务器
　　　　logging.handlers.SMTPHandler ：将日志消息发送给一个指定的email地址
　　　　logging.NullHandler ：该Handler实例会忽略error messages，通常被想使用logging的library开发者使用来避免'No handlers could be found for logger XXX'信息的出现。

·Format类
　　·直接实例化
　　·可以继承Format添加特殊内容
　　·三个参数
　　　　·fmt：指定消息格式化字符串，如果不指定该参数则默认使用message的原始值
        ·datefmt：指定日期格式字符串，如果不指定该参数则默认使用"%Y-%m-%d %H:%M:%S"
        ·style：Python 3.2新增的参数，可取值为 '%', '{'和 '$'，如果不指定该参数则默认使用'%' 

·Filter类
　　·可以被Handler和Logger使用
　　·控制传递归来的信息的具体内容
    ·案例02

import logging
import logging.handlers
import datetime

 

#定义logger
logger = logging.getLogger("mylogger")
logger.setLevel(logging.DEBUG)