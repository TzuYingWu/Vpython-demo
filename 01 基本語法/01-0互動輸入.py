# -*- coding:utf-8 -*-  

# #後方文字以及" "雙引號之間的內容為註釋，可在內寫上自己的筆記
# 三引號或三雙引號'''X#$%@'''或是"""X#$%@"""內的文字使用雙引號、單引號皆不影響code本體

"""
Auther   :吳姿瑩
Date     :2022/08/17
version  :python3.10.6
chapter  :python 互動輸入
"""

"""
1.輸入文字顯現出文字
"""
message = input("請輸入自己的名字：") #雙引號為文字串，表示文字的資料

print(message)



"""
2.顯示兩串結合的文字
"""
character = input("請輸入形容自己的形容詞：")
print(character)
print("Hello ! " +character+ "的" + message + " !")

