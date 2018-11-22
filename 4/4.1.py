from random import*
dim=randint(0,9)
count=0
while True:
    abc=eval(input("请输入一个数"))
    if abc > dim:
        print("大")
        count=count+1
    elif abc<dim:
        print("小")
        count=count+1
    else:
        count=count+1
        print("中")
        print(format(count))
        break
  

https://github.com/javafalcon/pythonProgram/tree/master/TextbookExercise
