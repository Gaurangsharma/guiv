n = int(input())
s = list(input())
l = len(s)
c = [[0 for i in range(26)] for i in range(l+1)]
for i in range(l):
    for j in range(26):
        c[i+1][j] = c[i][j]
    c[i+1][ord(s[i])-97]+=1
count = 0
for i in range(l):
    equals = 0
    for j in range(26):
        if c[i+1][j]-c[0][j]==c[l][j]-c[i+1][j] and c[i+1][j]!=0:
            equals+=1
    if equals>=n:
        count+=1
print(count)