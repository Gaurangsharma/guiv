def add(n):
    abc = 0
    for i in str(n):
        abc+=int(i)
    if str(abc)[0]=='1':
        return abc
    else:
        return False
n = int(input())
x = [8]
count = 0
iff = 2
urr = 800
while urr+iff<=n:
    urr+=iff
    w = add(urr)
    if w!=False:
        x.append(w)
        count+=1
    iff+=2
print(*x)
print(count)