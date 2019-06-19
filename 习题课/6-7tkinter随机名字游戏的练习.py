# -*- coding:utf-8 -*-
# @Time  ：2019/6/7 17:15
# @Author: Athany
# @File  : 6-7tkinter随机名字游戏的练习.py


# 用tkinter写一个小游戏，来随机生成我们需要的名字
import tkinter as tk
import random


window = tk.Tk()


def random_1():
    s1 = ["cats", "hippos", "cakes"]
    s = random.choice(s1)
    return s


def random_2():
    s2 = ["eats", "likes", "hates", "has"]
    s = random.choice(s2)
    return s


def button_click():
    name = nameEntry.get()
    verb = random_1()
    noun = random_2()
    sentence = name + verb + noun
    result.delete(0, tk.END)  # 把之前输出框里的结果从开始到结尾全部删除
    result.insert(0, sentence)


nameLabel = tk.Label(window, text="Name:")
nameEntry = tk.Entry(window)
button = tk.Button(window, text="生成随机名称", command=button_click)
result = tk.Entry(window)

nameLabel.pack()
nameEntry.pack()
button.pack()
result.pack()


window.mainloop()
