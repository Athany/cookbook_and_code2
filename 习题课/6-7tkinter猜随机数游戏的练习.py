# -*- coding:utf-8 -*-
# @Time  ：2019/6/7 21:38
# @Author: Athany
# @File  : 6-7tkinter猜随机数游戏的练习.py


# 一个猜数字的小游戏，让计算机随机生成一个整数，用户输入去猜这个整数，如果用户输入正确，则分数加一，并且显示出这个随机数
# 如果用户输入不正确，则分数不变，并且也显示出系统生成的随机数

import random
import tkinter as tk


window = tk.Tk()
maxNO = 10
score = 0
rounds = 0


def button_click():
    global score
    global rounds

    try:
        guess = int(guessBox.get())
        if 0 < guess < maxNO:
            result = random.randrange(1, maxNO+1)
            if guess == result:
                score += 1
            rounds += 1
        else:
            result = "输入不合法"
            rounds += 1

    except:
        result = "输入不合法"
        rounds += 1

    resultLabel.config(text="结果为：" + str(result))
    scoreLabel.config(text="得分：" + str(score) + "/" + str(rounds))
    guessBox.delete(0, tk.END)


scoreLabel = tk.Label(window)
resultLabel = tk.Label(window)
guessBox = tk.Entry(window)
guessLabel = tk.Label(window, text="请输入1到" + str(maxNO) + "的数字")
button = tk.Button(window, text="猜猜看", command=button_click)

scoreLabel.pack()
resultLabel.pack()
guessBox.pack()
guessLabel.pack()
button.pack()


window.mainloop()
