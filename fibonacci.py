n=int(input())
f1=1
f2=1
l=[]
l.append(f1)
l.append(f2)
s=f1+f2
for i in range(2,n):
    f1=f2
    f2=s
    s=f1+f2
    l.append(s)
for j in l:
    print(j,end=' ')
