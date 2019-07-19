# -*- coding:utf-8 -*-
# @Time  ：2019/7/18 15:36
# @Author: Athany
# @File  : 7.18-Spider-selenium-豆瓣读书.py

"""
url = "https://book.douban.com/subject_search?search_text=python&cat=1001"
使用selenium爬取页面
保存内容用xpath进行分析
"""

from selenium import webdriver
import time
from lxml import etree

def get_web(url):
    driver = webdriver.Chrome()
    driver.get(url)

    time.sleep(5)

    driver.save_screenshot("douban_reader.png")

    fn = "douban_reader.html"
    with open(fn, "w", encoding="utf-8") as f:
        f.write(driver.page_source)

    content_parse(fn)
    driver.quit()

def content_parse(fn):
    # html = ""

    with open(fn, "r", encoding="utf-8") as f:
        html = f.read()

    # 生成xml数
    tree = etree.HTML(html)

    # 查找book
    books = tree.xpath("//div[@class='item-root']")

    for book in books:
        book_name = book.xpath(".//div[@class='title']/a")
        print(book_name[0].text)

if __name__ == '__main__':
    url = 'https://book.douban.com/subject_search?search_text=python&cat=1001'
    get_web(url)
