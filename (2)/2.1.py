#e1.1TempConvert.py
TempStr=(input("请输入温度:"))
if TempStr[-1] in ['F','f']:
    C=(eval(TempStr[0:-1]) - 32)/1.8
    print("转换后的温度是{:.0f}C".format(C))
elif TempStr[-1] in ['C','c']:
    F=1.8*eval(TemtStr[0:-1]) +32
    print("转换后的温度是{:.0f}F".format(F))
else:
    print("输入格式有误")
