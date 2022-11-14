# -*- coding: utf-8 -*-
# @Time    : 2022/11/12
# @Author  : Lc
# @Software: PyCharm
# @File    : gen.py


import pyperclip
import re

strx = pyperclip.paste()
# print(strx)
# hs = strx.splitlines()
stry = re.findall(r'[A-Za-z0-9]{32}', strx, re.M)

# print(stry)
print(str(stry))
pyperclip.copy(str(stry))
