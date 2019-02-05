s = input().strip()
count = 0
for k in range(len(s)-1):
    if s[k] in 'aeiou' and s[k+1] in 'aeiou' :
        count += 1
print(count)
