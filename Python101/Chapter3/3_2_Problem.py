k = 1
p = 1.0
while 1-p < 0.5:
    p *= (365-k)/365
    k += 1
print(k)
