a,b = [int(e) for e in input().split()]
sum = 0
for i in range(a,b):
    t = 0
    for j in range(i+1,b+1):
        t += (i+j)
    sum += (-1)**i*t
print(sum)
