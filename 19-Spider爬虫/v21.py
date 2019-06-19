from urllib import request
import json
#指定开始位置和结束位置：start开始的视频  limit：即每页显示的视频数量（默认每页是20个可以自己设定每页显示的数值）
url='https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&start=0&limit=20'
"""
param={

    'type':'13',
    'interval_id':'100:90',
    'action':'',
    'start':'0',  # 指定开始爬取的开始位置
    'limit':'20', # 默认每页的显示的视频个数

}
"""

response = request.urlopen(url)
data = response.read().decode()

data = json.loads(data)

print(data)
