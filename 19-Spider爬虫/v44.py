from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")

driver.get("https://www.baidu.com")

text = driver.find_element_by_id("wrapper").text

"""
新闻
hao123
地图
视频
贴吧
学术
登录
设置
更多产品
百度
把百度设为主页关于百度About  Baidu百度推广
©2018 Baidu 使用百度前必读 意见反馈 京ICP证030173号  京公网安备11000002000001号 
"""
print(text)
# 百度一下，你就知道
print(driver.title)

# 输入 大熊猫--3s ---点击---5s --daxiongmao.png
# ctrl+a ---2s --ctrl+x ---2s
# 输入 航空母舰 ->截图hangmu.png--回车--5s--截图hangmushow.png
# 清空输入框 -截图--退出


# 得到页面的快照
# driver.save_screenshot("index.png")
# id ='kw' 是百度搜索的按钮,我们得到输入框的ui 元素后直接输入大熊猫
driver.find_element_by_id("kw").send_keys(u"大熊猫")
time.sleep(3)
# id='su' 是百度搜索的按钮,click 模拟点击
driver.find_element_by_id("su").click()

time.sleep(5)
driver.save_screenshot("daxiongmao.png")

# 获取当前页面的cookie
print(driver.get_cookies())

# 模拟ctr+a
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')
time.sleep(2)
# 模拟ctr+X
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')
time.sleep(2)

driver.find_element_by_id("kw").send_keys(u"航空母舰")
driver.save_screenshot("hangmu.png")

driver.find_element_by_id("su").send_keys(Keys.RETURN)
time.sleep(5)
driver.save_screenshot("hangmushow.png")

# 清空输入框
driver.find_element_by_id("kw").clear()
driver.save_screenshot("clear.png")

driver.quit()
