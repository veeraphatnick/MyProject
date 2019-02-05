x,y = [float(e) for e in input().split()]
if(x==0 and y==0):
    print('center')
elif(x==0):
    print('on X')
elif(y==0):
    print('on Y')
elif(x>0 and y>0):
    print('1')
elif(x<0 and y>0):
    print('2')
elif(x<0 and y<0):
    print('3')
else:
    print('4')
