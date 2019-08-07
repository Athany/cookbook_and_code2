# -*- coding:utf-8 -*-
# @Time  ：2019/7/22 18:23
# @Author: Athany
# @File  : 7.22-Spider-selenium-爬豆瓣.py

"""
任务：
1.利用selenium模拟鼠标下拉
2.每次都出现电影的信息
"""

from selenium import webdriver
import time

url = "https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action="

driver = webdriver.Chrome()
driver.get(url)

# 向下滚动1万像素
js = "document.body.scrollTop=10000"
time.sleep(3)

driver.save_screenshot("douban1.png")

driver.execute_script(js)
time.sleep(3)

driver.save_screenshot("douban2.png")
driver.quit()
