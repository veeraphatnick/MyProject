a,b,c,d = [float(e) for e in input().split()]
max = a
if b > max : max = b
if c > max : max = c
if d > max : max = d
min = a
if b < min : min = b
if c < min : min = c
if d < min : min = d
sum = (a+b+c+d)-max-min
print(sum)
