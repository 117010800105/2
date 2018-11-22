a=0
b=0
c=0
d=0
e=input("")
for i in range(len(e)):
    if e[i]==" ":
        a=a+1
    elif "A" <e[i] <= "Z" or "a" <e[i]<= "z":
        b=b+1
    elif "0"<=e[i]<="9":
        c=c+1
    else:
        d=d+1
print("{}{}{}{}".format(a,b,c,d))
