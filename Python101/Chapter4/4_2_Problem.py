s = input().strip()
t = ''
s = ' '+ s +' '
for i in range(1,len(s)-1):
    t += s[i]
    if s[i-1] != s[i] != s[i+1 ]:
        t += s[i]
print(t)
