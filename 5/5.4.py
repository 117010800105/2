def multi(*a): #发表示a可变
    if len(a) == 0:
        return 0
    t = 1
    for i in a:
        t = t * i
    return t

print( multi(1,2,3,4,5,6,7,8,9,10))
