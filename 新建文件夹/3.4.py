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
    
    
    
n = input("输入一个5位数字: ")
j = -1
f = 1 #标志变量
for i in range(5):
    if n[i]  != n[j]:
        f = 0
    j = j - 1

if f == 1:
    print("{}是回文数".format(n))
else:
    print("{}不是回文数".format(n))
    
 n = input("输入一个5位数字: ")   
m=n[::-1]
if n=m:
     print("{}是回文数".format(n))
else:
    print("{}不是回文数".format(n))
