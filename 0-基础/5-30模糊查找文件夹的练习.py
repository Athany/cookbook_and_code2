# -*- coding:utf-8 -*-
# @Time  ：2019/5/30 2:40
# @Author: Athany
# @File  : 5-30模糊查找文件夹的练习.py

import os

start_dir = input("请输入目录：")
target = input("请输入您要搜索的文件名：")


def search_file(start_dir, target):
    os.chdir(start_dir)

    for each_file in os.listdir(os.curdir):

        if target in each_file:
            print(os.getcwd() + os.sep + each_file)

        if os.path.isdir(each_file):
            search_file(each_file, target)
            os.chdir(os.pardir)


search_file(start_dir, target)


