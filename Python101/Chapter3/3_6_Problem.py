n = int(input())
a = int(input())
max = min = a
count = 0
if a < 0 : count = 1
for i in range(1,n+1):
    a = int(input())
    if a > max : max = a
    if a < min : min = a
    if a < 0 : count += 1
print((max - min),c)
