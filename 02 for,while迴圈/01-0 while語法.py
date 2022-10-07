"""
Auther   :吳姿瑩
Date     :2022/10/07
version  :python3.10.6
chapter  :python while寫法
"""

"""
1.while 條件
"""
result = 0
i = 0           #初始值
n = 10          #設定範圍

while i <= n :
        print("i= ",i)
        result += i
        i += 1

print("result = ", result)
