#e3.6TextProgress Bar.py
import time
scale=10
print("------执开始行------")
for i in range(scale+1):
    a,b= 'gfgfd' * i,'..'* (scale-i)
    c=(i/scale)*100
    print("%{:^3.0f}[{}->{}]".format (c ,a , b))
    time.sleep(0.1)
print("------执行结束------")


mport time
scale = 50
t = time.clock()
for i in range(scale + 1):
    a = '.' * i
    c = (i / scale) * 100
    t -= time.clock()
    print("\rStarting {:^3.0f}%[{}]{:.2f}s Done".format(c,a,-t), end='')
    time.sleep(0.05)
    
    
    
