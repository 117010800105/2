def isNum(s):
    try:
        n = eval(s)
    except:
        return False
    return True
s = input("")
if isNum(s):
    print("number")
else:
    print("not a number")
