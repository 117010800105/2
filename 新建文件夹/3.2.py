#e3.2DayDayUp365.py
import math
dayup,dayfactor=1.0,0.01
for i in range(365):
    if i % 7 in [1,2,3]:
        dayup = dayup
    else:
        dayup = dayup * (1+dayfactor)
print("能力值:{:.2f}.".format(dayup))
    
