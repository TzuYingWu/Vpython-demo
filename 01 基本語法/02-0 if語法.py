"""
Auther   :吳姿瑩
Date     :2022/08/17
version  :python3.10.6
chapter  :python if語法
"""

"""
1.輸入兩個數值
"""
# 由使用者輸入 a , b 量值的寫法

a = int(input("請輸入一個整數a(-100~100) : "))
b = int(input("請輸入一個整數b(-100~100) : "))



"""
2.輸入 a , b 比大小(if 一層)
"""
#if (一層)
if(a > b):
    print("一層檢驗a > b")
else:
    print("一層檢驗a <= b")


"""
3.輸入 a , b 比大小(if 兩層)
"""
#if (兩層)
if(a > b):
    print("兩層檢驗a > b")
elif(a ==b):
    print("兩層檢驗a == b")
else:
    print("兩層檢驗a < b")
