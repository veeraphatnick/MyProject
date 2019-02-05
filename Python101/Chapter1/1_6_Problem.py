import math
r,theta = [float(e) for e in input().split()]
x = r*math.cos(theta)
y = r*math.sin(theta)
print(x, y)
