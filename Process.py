# -*- coding: utf-8 -*-
# @Time    : 2022/10/2
# @Author  : Lc
# @Software: PyCharm
# @File    : Process.py

import multiprocessing

import time


# 2个要同时执行的函数
def music():
    for i in range(5):  # 执行5次
        print("A...")
        time.sleep(0.2)  # 延迟0.2s，目的是让效果对比更明显一些


def movie():
    for i in range(5):
        print("B...")
        time.sleep(0.2)  # 延迟0.2s


if __name__ == "__main__":  # 解决Windows系统下调用包时的递归问题
    # 创建子进程
    music_process = multiprocessing.Process(target=music)
    movie_process = multiprocessing.Process(target=movie)

    # 启用进程
    music_process.start()
    movie_process.start()

    print("主进程执行完毕")
