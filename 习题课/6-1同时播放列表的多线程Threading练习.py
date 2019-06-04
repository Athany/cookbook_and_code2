# -*- coding:utf-8 -*-
# @Time  ：2019/6/1 22:56
# @Author: Athany
# @File  : 6-1同时播放列表的多线程Threading练习.py

import threading
import time

movie_list = ["斗破苍穹.mp4", "复仇者联盟.avi", "钢铁侠.rmvb", "反贪风暴4.mp4"]
music_list = ["丑八怪.mp3", "凤凰传奇.mp3", "我们不一样.acc"]
movie_format = ["mp4", "avi"]
music_format = ["mp3"]


def play(playlist):
    for i in playlist:
        if i.split(".")[1] in movie_format:
            print("您现在收看的是：{}.".format(i))
            time.sleep(3)
        elif i.split(".")[1] in music_format:
            print("您现在收听的是：{}。".format(i))
            time.sleep(2)
        else:
            print("没有可播放的格式")


def thread_run():
    t1 = threading.Thread(target=play, args=(movie_list,))
    t2 = threading.Thread(target=play, args=(music_list,))
    t1.start()
    t2.start()


if __name__ == "__main__":
    thread_run()