# -*- coding: utf-8 -*-
# @Time    : 2022/11/29
# @Author  : Lc
# @Software: PyCharm
# @File    : request.py


import requests

s = requests.session()
s.cookies.set('mycookie', 'value')  # 设置会话cookies
r = s.get('https://www.baidu.com')
print(s.cookies.get_dict())  # 输出cookies

c = requests.cookies.RequestsCookieJar()  # 定义一个cookie对象
c.set('cookie-name', 'cookie-value')  # 增加cookie的值
s.cookies.update(c)  # 更新s的cookie
print(s.cookies.get_dict())  # 更新后

s.cookies.clear()  # 删除cookies,也可以使用s.cookies=None的方式将所有cookies删除
print(s.cookies.get_dict())  # 删除后

s.get('https://www.baidu.com')
print(s.cookies.get_dict())  # 删除前
s.cookies.set('BDORZ', None)  # 删除cookies中BDORZ的值
print(s.cookies.get_dict())  # 删除后
