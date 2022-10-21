"""
Auther   :吳姿瑩
Date     :2022/10/21
version  :python3.10.6 vpython7
chapter  :環境設置
"""
from vpython import *

#t = text(text='Faces forward', pos=vec(-4,0,0),color=color.cyan, billboard=True, emissive=True)
#屏幕默認大小和背景颜色
#注意vec=vector

text(text='Hello World', pos=vec(0,0,0),color=color.cyan, billboard=True, emissive=True)

text(text='Hello World', pos=vec(0,5,0),color=color.hsv_to_rgb(vector (60/255, 100/255, 100/255)) , billboard=True, emissive=True)

