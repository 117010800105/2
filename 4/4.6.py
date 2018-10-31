import random
a="113"
c=0
for i in range(10000):
    b=random.sample(a,1)
    if b ==['1']:
        c=c+1
d=c/10000
print("更换{}%".format(d*100))
c=0
for i in range(10000):
    b=random.sample(a,1)
    if b ==['3']:
        c=c+1
d=c/10000
print("不更换{}%".format(d*100))
