x1,y1,r1 = [float(e) for e in input().split()]
x2,y2,r2 = [float(e) for e in input().split()]
d = (x1-x2)**2+(y1-y2)**2
sum_r = (r1+r2)**2
if(d < sum_r):
    print('overlap')
elif(d == sum_r):
    print('touch')
else:
    print('free')
