p = 0.0
for k in range(1,400000,4):
    p += 1/k
    p -= 1/(k+2)
print(4*p)
