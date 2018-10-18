while True:
    for i in ["/" , "-","|","\\", "|"]:
        print("%s\r" % i, end= '' )

        
#\r:回车  %s：是用在“格式化字符串”里的。用法实例：
#name="Tom"
#print"Hello%s"%name在第二行中print了一个格式化字符串，把name变量的内容替换到%s处。打印出
#来就是：Hello Tom
