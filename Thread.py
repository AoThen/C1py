# -*- coding: utf-8 -*-
# @Time    : 2022/10/2
# @Author  : Lc
# @Software: PyCharm
# @File    : Thread.py


import threading

import time


def music(name, loop):
    for i in range(loop):
        print("A %s , 第%s次" % (name, i))
        time.sleep(0.2)


def movie(name, loop):
    for i in range(loop):
        print("B%s , 第%s次" % (name, i))
        time.sleep(0.2)


if __name__ == "__main__":
    music_thread = threading.Thread(target=music, args=("X", 3))
    movie_thread = threading.Thread(target=movie, args=("Y", 3))
    music_thread.start()
    movie_thread.start()
    print("主线程执行完毕")
