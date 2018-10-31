from random import*
dim=randint(0,100)
while True:
    abc=int(input("请输入一个数"))
    if abc > dim:
        print("大")
    elif abc<dim:
        print("小")
    else:
        print("中")
except: 
    print("输入一个整数")
