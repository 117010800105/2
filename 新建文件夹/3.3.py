#e3.2DayDayup.py
import math
dayup,dayfactor=1.0,0.005
for i in range(365):
    if i %15 in [0]:
        dayup=dayup * (1-dayfactor)
    else:
        dayup=dayup* (1+dayfactor)
print("上15下1: {:.2f}.".format(dayup))
#e3.2DayDayup.py
import math
dayup,dayfactor=1.0,0.005
for i in range(365):
    if i %10 in [0]:
        dayup=dayup * (1-dayfactor)
    else:
        dayup=dayup * (1+dayfactor)
print("上10下1: {:.2f}.".format(dayup))

dayup, dayfactor = 1.0, 0.01
for i in range(1,366):  #0-6 7天  1-7 7
    if i % 10 in [4,5,6,7]:
        dayup = dayup * (1 + dayfactor)
    print("{}：天的能力{}".format(i+1,dayup))
    
    
    dayup, dayfactor = 1.0, 0.01
for i in range(1,366):  #0-6 7天 1-7 7
    if i % 15 in [4,5,6,7,8,9,10,11,12]:
 dayup = dayup * (1 + dayfactor)
    print("{}：能力{}".format(i+1,dayup))



