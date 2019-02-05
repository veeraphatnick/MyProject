#file1 = open(input().strip())
#file1 = open('C:\\Users\\58050379\PycharmProjects\Chapter5\\5_1_File','r')
file1 = open('C:/Users/58050379\PycharmProjects/Chapter5/5_1_File','r')
s = ''
for line in file1:
    if line[-1] != '\n' :
        line = line + '\n'
    s = line + s
file1.close()
print(s[:-1])
