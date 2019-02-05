d,n = [int(e) for e in input().split()]
t = "0"*n + str(d)
t = t[-max(n,len(str(d))):]
print(t)
