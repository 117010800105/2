def isOdd(n):
    if n%2 == 1:
        return True
    else:
        return False
n=eval(input(""))
if isOdd(n):
    print("奇数")
else:
    print("偶数")
