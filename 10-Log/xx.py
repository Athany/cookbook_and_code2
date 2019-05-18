# -*- coding:utf-8 -*-
colors = ["red", "yellow", "green", "blue"]

for color in colors:
    if color == "green":
        print("绿色")
    else:
        print("这个不是绿色，这个是{}。".format(color))
if __name__ == '__main__':
    print("运行结束")