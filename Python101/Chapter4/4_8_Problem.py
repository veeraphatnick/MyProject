s = input().strip()
s = s[::-1]
d = 0
for i in range(len(s)) :
    if s[i] in '23456789':
        d = ('Error input = 0,1')
        break
    else :
        d += int(s[i])*2**i
if d != 0:
    print(d)
