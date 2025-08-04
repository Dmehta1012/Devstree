# ((x2 - x1)**2 + (y2 - y1)**2)**0.5
import math

x1=float(input("Enter x1 value "))
x2=float(input("Enter y1 value "))
t1=("x1,y1")
y1=float(input("Enter x2 value "))
y2=float(input("Enter y2 value "))
t2=("x2,y2")
    
dis=((x2 - x1)**2 + (y2 - y1)**2)**0.5

print(f"your {t1} and {t2}  distane is:{dis :2f} units" )