n=list(input().split()) 
l=[] 
for i in n:
    for j in i:
        l.append(j)
    l.reverse()
    print(*l,sep='',end=' ')
    l=[]