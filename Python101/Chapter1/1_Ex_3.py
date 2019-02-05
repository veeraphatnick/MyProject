import math
a = float(input())
b = float(input())
D = float(input())
C = D*math.pi/180
c = math.sqrt((a**2+b**2)-(2*a*b*math.cos(C)))
print("c = ",c,"cm.")
