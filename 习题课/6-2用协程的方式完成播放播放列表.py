# -*- coding:utf-8 -*-
# @Time  ：2019/6/2 21:33
# @Author: Athany
# @File  : 6-2用协程的方式完成播放播放列表.py

# 用协程的方式完成播放播放列表

import asyncio
import time
# asyncio await

movie_list = ["斗破苍穹.mp4", "复仇者联盟.avi", "钢铁侠.rmvb", "反贪风暴4.mp4"]
music_list = ["丑八怪.mp3", "凤凰传奇.mp3", "我们不一样.acc"]
movie_format = ["mp4", "avi"]
music_format = ["mp3"]


@asyncio.coroutine
def play(playlist):
    for i in playlist:
        if i.split(".")[1] in movie_format:
            print("您现在正在收看的是{}。".format(i))
            yield time.sleep(3)

        elif i.split(".")[1] in music_format:
            print("您现在正在收听的是{}。".format(i))
            yield time.sleep(2)

        else:
            print("没有可支持播放的格式")


loop = asyncio.get_event_loop()
task = [play(movie_list), play(music_list)]
loop.run_until_complete(asyncio.wait(task))
loop.close()
