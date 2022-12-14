import math
x = float (input("BC:"))
y = float (input("AC:"))
a = math.atan(x/y)
b = (a*180/math.pi)
c = (180-(90+b))
print("BAC=",b)
print("ABC=",c)
