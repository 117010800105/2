#e1.1TempConvert.py
money=input("gyjjyu:")
if money[-3:] in ['rmb','RMB']:
    dollor= eval(money[0:-3])*6
    print("ikado{:.2f}dollar".format(dollor))
elif money[-6:] in ['dollar','DOLLAR']:
    rmb=eval(money[0:-6])/6
    print("ikado{:.2f}rmb".format(rmb))
else:
    print("forse")
