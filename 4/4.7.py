from random import*
dim=randint(0,9)
try:
    while True:
        abc=int(input("请输入一个数"))
        if abc > dim:
            print("大")
        elif abc<dim:
            print("小")
        else:
            print("中")
except NameError:
    print("请输入一个整数")
else:
    print("没有发生异常")
finally:
    print("程序执行完毕，不知有没有发生异常")
  

