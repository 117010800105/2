#3.4.py
import math
TempStr=input("输入一个五位数：")
if TempStr[0] in TempStr[-1]:
    if TempStr[1] in TempStr[-2]:
        print("yes")
    else:
        print("no")
else:
    print("no")
