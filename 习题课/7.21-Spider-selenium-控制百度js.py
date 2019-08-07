# -*- coding:utf-8 -*-
# @Time  ：2019/7/21 23:09
# @Author: Athany
# @File  : 7.21-Spider-selenium-控制百度js.py

"""
任务：
1.通过selenium模拟对页面元素的控制
"""

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")

# 通过js来控制网页内容
# 需要先把js编写出来
# 然后通过execute_script执行

# 美化输入框，输入框id是kw
js = "var q=document.getElementById(\'kw\'); q.style.border=\'2px solid red\';"

# 执行代码
driver.execute_script(js)

time.sleep(3)
driver.save_screenshot('redbaidu.png')

# js隐藏相应元素，这里隐藏logo
img = driver.find_element_by_xpath('//*[@id="lg"]/img')
driver.execute_script('$(arguments[0]).fadeOut()', img)
time.sleep(2)
# 滚动华东条到最底下
js = "$('.scroll_top').click(function(){$('html, body').animate({scrollTop:'0px'}, 800)});"

# 查看网页快照
time.sleep(3)
driver.save_screenshot("nullbaidu.png")
