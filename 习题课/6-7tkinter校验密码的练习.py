# -*- coding:utf-8 -*-
# @Time  ：2019/6/7 21:14
# @Author: Athany
# @File  : 6-7tkinter校验密码的练习.py


import tkinter as tk

window = tk.Tk()


def check_password():
    password = "123456"
    entered_password = passwordEntry.get()
    if entered_password == password:
        confirmLabel.config(text="正确")
    else:
        confirmLabel.config(text="不正确")
        passwordEntry.delete(0, tk.END)


passwordLabel = tk.Label(window, text="密码：")
passwordEntry = tk.Entry(window, show="*")
button = tk.Button(window, text="校验", command=check_password)
confirmLabel = tk.Label(window)

passwordLabel.pack()
passwordEntry.pack()
button.pack()
confirmLabel.pack()

window.mainloop()
