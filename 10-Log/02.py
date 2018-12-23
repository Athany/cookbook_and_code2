'''
1. 需求

现在有以下几个日志记录的需求：

1）要求将所有级别的所有日志都写入磁盘文件中

2）all.log文件中记录所有的日志信息，日志格式为：日期和时间 - 日志级别 - 日志信息

3）error.log文件中单独记录error及以上级别的日志信息，日志格式为：日期和时间 - 日志级别 - 文件名[:行号] - 日志信息

4）要求all.log在每天凌晨进行日志切割
2. 分析

1）要记录所有级别的日志，因此日志器的有效level需要设置为最低级别--DEBUG;

2）日志需要被发送到两个不同的目的地，因此需要为日志器设置两个handler；另外，两个目的地都是磁盘文件，因此这两个handler都是与FileHandler相关的；

3）all.log要求按照时间进行日志切割，因此他需要用logging.handlers.TimedRotatingFileHandler; 而error.log没有要求日志切割，因此可以使用FileHandler;

4）两个日志文件的格式不同，因此需要对这两个handler分别设置格式器；

'''

import logging
import logging.handlers
import datetime
# 创建日志器
import sys

logger = logging.getLogger('mylogger')
# 配置日志器级别
logger.setLevel(logging.DEBUG)

# 创建handler处理器

first_handler = logging.FileHandler(filename='error.log')  # 设置名称
first_handler.setLevel(level=logging.ERROR)  # 给处理器设置级别
first_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(module)s[%(lineno)d] - %(message)s'))

second_handler = logging.handlers.TimedRotatingFileHandler(filename='all.log', when='midnight', interval=1,backupCount=7, atTime=datetime.time(0, 0, 0, 0))
second_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
# 输出到控制台
third_handler = logging.StreamHandler()
third_handler.setLevel(level=logging.ERROR)

# 配置处理器
logger.addHandler(first_handler)
logger.addHandler(second_handler)
logger.addHandler(third_handler)
# 创建记录
logger.debug('debug msg')
logger.info(' this is info')
logger.warning(' warning')
logger.error('error bug BUG')
logger.critical('critical')
