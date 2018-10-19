#e3.2DayDayUp365.py
import math
dayup,dayfactor=1.0,0.01
for i in range(365):
    if i % 7 in [1,2,3]:
        dayup = dayup
    else:
        dayup = dayup * (1+dayfactor)
print("能力值:{:.2f}.".format(dayup))
    
dayup, dayfactor = 1.0, 0.01
for i in range(1,366):
    if i % 50 in [0,1,2,3]:
        dayup = dayup
    elif i % 7 in [0,6,5,4]:
        dayup = dayup * (1 + dayfactor)
print("连续学习3天能力值不变，从第4天至第7天每天能力增长为前一天1%的力量: {:.2f}.".format(dayup))
