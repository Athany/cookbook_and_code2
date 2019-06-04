# -*- coding:utf-8 -*-
# @Time  ：2019/5/30 2:13
# @Author: Athany
# @File  : 5.30查找文件的练习.py

import os, sys
sys.setrecursionlimit(500)

start_dir = input("请输入目录：")
target = input("请输入要搜索的文件名：")


def search_file(start_dir, target):
    os.chdir(start_dir)  # 切换到用户输入的路径  # os.chdir() 方法用于改变当前工作目录到指定的路径。change directory

    for each_file in os.listdir(os.curdir):
        if each_file == target:
            print(os.getcwd() + "\\" + each_file)  # os.getcwd() 方法用于返回当前工作目录。

        if os.path.isdir(each_file):
            search_file(each_file, target)  # 递归调用
            os.chdir(os.pardir)  # 获取当前目录的父目录字符串名：('..')   https://www.jb51.net/article/57995.htm


search_file(start_dir, target)
