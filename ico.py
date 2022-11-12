# -*- coding: utf-8 -*-
# @Time    : 2022/11/10
# @Author  : Lc
# @Software: PyCharm
# @File    : ico.py

import base64

# pillow
from PIL import Image


# 将图片转换成base64
def img_to_base64(path):
  with open(path, "rb") as f:
    base64_data = base64.b64encode(f.read())
    return f'data:image/jpg;base64,{base64_data.decode()}'


img = Image.open("1.png")
width = img.size[0]  # 获取宽度
height = img.size[1]  # 获取高度
img = img.resize((int(width * 0.1), int(height * 0.1)), Image.ANTIALIAS)
img.save("2.png", bitmap_format='png')

print(img_to_base64("2.png"))
