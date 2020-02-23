l=[]
for _ in range(6):
    l.append(list(map(str,input().split())))
l2=l[::-1]
ans=[]
for i in range(len(l2)):
    s=str(l2[i])
    k= s[::-1]
    ans.append(list(k[1:len(k)-1]))

for i in ans:
    i=i[1:len(i)-1]
    print(*i,sep='')