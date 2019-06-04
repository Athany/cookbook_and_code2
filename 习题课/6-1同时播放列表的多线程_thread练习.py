# -*- coding:utf-8 -*-
# @Time  ：2019/6/1 14:31
# @Author: Athany
# @File  : 6-1同时播放列表的多线程_thread练习.py
import _thread as thread
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
    thread.start_new_thread(play, (movie_list,))
    thread.start_new_thread(play, (music_list,))
    while True:
        time.sleep(7)



if __name__ == "__main__":
    thread_run()