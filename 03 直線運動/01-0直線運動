"""
Auther   :吳姿瑩
Date     :2022/08/17
version  :python3.10.6 vpython7
chapter  :直線運動
"""

from vpython import *

"""
 1. 參數設定, 設定變數及初始值
"""
size = 0.05   # 木塊邊長
L = 1.55      # 地板長度
v = 0.05      # 木塊速度
t = 0         # 時間
dt = 0.01     # 時間間隔



"""
 2. 畫面設定
"""
#畫面設定，預設為 640 and 400 像素
#scene:backgroung有三個數字唯色碼表，https://www.ifreesite.com/color/online-color-picker.htm
scene = canvas(title="1D Motion", width=640, height=400, x=0, y=0, center=vec(0, 0.3, 0), background=vec(204/255,204/255,255/255))
floor = box(pos=vec(0, 0, 0), size=vec(L, 0.01*size, 0.5*L), color=color.green)
cube = box(pos=vec(-0.5*L + 0.5*size, 0.5*size+0.01*size, 0), length=size, height=size, width=size, color=color.red, v=vec(v, 0, 0))
#畫x-t圖v-t圖設定畫布
#找停止時間，設置x-t圖，x軸最大值
gd = graph(title="x-t plot", width=600, height=450,xmax=35, x=0, y=600, xtitle="t(s)", ytitle="x(m)")
gd2 = graph(title="v-t plot", width=600, height=450,ymin=0, ymax=0.1, x=0, y=1050, xtitle="t(s)", ytitle="v(m/s)")
xt = gcurve(graph=gd, color=color.red)
vt = gcurve(graph=gd2, color=color.red)



"""
 3. 物體運動部分, 木塊到達地板邊緣時停止執行
"""
while(cube.pos.x <= 0.5*L- 0.5*size):
    rate(1000)
    cube.pos.x += v*dt          #x=x0+v*dt
    xt.plot(pos = (t, cube.pos.x))
    vt.plot(pos = (t, cube.v.x))
    t += dt

print("所需時間為t = ", t)
