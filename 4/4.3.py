a=eval(input(""))
b=eval(input(""))
if a<b:
    m,n=b,a
else:
    m,n=a,b
r=m%n
while(r!=0):
    m,n=n,r
    r=m%n
print("{}".format(n))
print("{}".format(a*b/n))
