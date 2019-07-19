# -*- coding:utf-8 -*-
# @Time  ：2019/7/18 16:26
# @Author: Athany
# @File  : 7.18-Spider-selenium-登陆豆瓣-已改js.py

"""
利用selenium模拟登陆豆瓣
需要输入验证码
思路：
1.保存页面成快照
2.等待用户手动输入验证码
3.继续自动执行提交等动作
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
url = "https://accounts.douban.com/passport/login"
driver = webdriver.Chrome()
driver.get(url)

time.sleep(3)

# 生成快照，用来查看验证码
driver.save_screenshot("douban_index.png")

captcha = input("请输入验证码：")

# 利用账户信息和验证码登陆
driver.find_element_by_id("email").send_keys("1366798119@qq.com")
driver.find_element_by_id("password").send_keys("haha123456")
driver.find_element_by_id("captcha_field").send_keys(captcha)

driver.find_element_by_xpath("//input[@class='btn-submit']").click()

time.sleep(5)

driver.save_screenshot("logined.png")

with open("douban_home.html", "w", encoding="utf-8") as file:
    file.write(driver.page_source)

driver.quit()
