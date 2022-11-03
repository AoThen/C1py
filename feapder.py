# -*- coding: utf-8 -*-
# @Time    : 2022/10/31
# @Author  : Lc
# @Software: PyCharm
# @File    : feapder.py


import time

import requests


class timeTaobao():
    r1 = requests.get(
        url='https://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp',
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36'}
    )
    x = r1.json()
    timeNum = int(x['data']['t'])

    @staticmethod
    def funcname():
        timeStamp = float(timeTaobao.timeNum / 1000)
        timeArray = time.localtime(timeStamp)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        return otherStyleTime


t = timeTaobao.funcname()
print('淘宝', t)
print('本地', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
