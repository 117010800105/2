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
        
        
        
n_alphabet = 0
n_alphabet = 0
n_number = 0
n_space = 0
n_other = 0
s = input('请输入一行字符')
for c in s:
    if 'A' <= c <= 'Z' or 'a' <= c <= 'z':
        n_alphabet += 1
    elif '0' <= c <= '9':
        n_number += 1
    elif c == ' ':
        n_space += 1
    else:
        n_other += 1
print('有{0}个英文字符，{1}个数字，{2}个空格和{3}个其它字符'.format(n_alphabet, n_number, n_space, n_other))


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


n1, n2 = eval(input('请输入两个整数，中间用逗号隔开：'))
x, y = n1, n2
r = x % y
while r > 0:
    x,y = y,r
    r = x % y

print('{}和{}最大公约数是：{}， 最小公倍数是：{}'.format(n1, n2, y, n1 * n2 / y))


3-
for i in range(11):
    if i in [0,5,10]:
        print("+ - - - - + - - - - +") # "+","-"*4,"+","-"*4,"+"
    else:
        print("|")

for i in range(11):
    for j in range(11):
        if i%5==0
            if j%5 ==0:
                print("+",end='')
            else:
                print("-",end='')
        else:
            if j%5 == 0:
                print("|",end='')
            else:
                print(" ",end='')
        

