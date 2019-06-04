# -*- coding:utf-8 -*-
# @Time  ：2019/5/29 21:40
# @Author: Athany
# @File  : 5-29全部替换功能的练习.py

file_name = input("请输入你要打开的文件名：")

rep_word = input("请输入你要替换的字符：")

new_word = input("请输入替换的新的字符：")


def file_replace(file_name, rep_word, new_word):
    f = open(file_name)
    content = []

    for eachline in f:

        if rep_word in eachline:
            # nonlocal new_eachline
            eachline = eachline.replace(rep_word, new_word)  # https://fishc.com.cn/thread-94943-1-243.html

        content.append(eachline)

    decide = input("你确定要这样做吗？请输入YES/NO: ")

    if decide in ["YES", "Yes", "yes", "Y", "y"]:
        f_write = open(file_name, "w")
        f_write.write("".join(content))
        f_write.close()


file_replace(file_name, rep_word, new_word)