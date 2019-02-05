n = input()
isbn = (10*int(n[0])+9*int(n[1])+8*int(n[2])+7*int(n[3])+6*int(n[4])+5*int(n[5])+4*int(n[6])\
    +3*int(n[7])+2*int(n[8]))
a = (int(isbn/11)+1)*11
b = a-isbn
print(str(n)+str(b))
