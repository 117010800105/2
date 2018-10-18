#e3.2DayDayup.py
import math
dayup,dayfactor=1.0,0.005
for i in range(365):
    if i %10 in [0]:
        dayup=dayup * (1-dayfactor)
    else:
        dayup=dayup * (1+dayfactor)
print("上10下1: {:.2f}.".format(dayup))


