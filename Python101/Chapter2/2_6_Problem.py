a = int(input())
x = int(round(a**(1/3),0))
if x**3 == a :
    print(x)
else:
    print('Not Found')
