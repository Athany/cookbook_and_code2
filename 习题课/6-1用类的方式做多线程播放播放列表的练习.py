# -*- coding:utf-8 -*-
# @Time  ：2019/6/1 23:14
# @Author: Athany
# @File  : 6-1用类的方式做多线程播放播放列表的练习.py

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


class MyThread(threading.Thread):
    def __init__(self, playlist):
        super().__init__()
        self.playlist = playlist

    def run(self):
        play(self.playlist)


if __name__ == "__main__":
    m1 = MyThread(movie_list)
    m2 = MyThread(music_list)
    m1.start()
    m2.start()
