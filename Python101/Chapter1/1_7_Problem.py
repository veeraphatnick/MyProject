import math
x,y = [float(e) for e in input().split()]
r = math.sqrt(x**2+y**2)
theta = math.atan2(y,x)
print(r,theta)
