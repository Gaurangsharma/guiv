n,m=map(int,input().split())
l=[]
ll,lll=[],[]
for i in range(n):
    l.append(list(map(int,input().split()))) 
for i in range(n):
    for j in range(m):
        if l[i][j]==0:
            ll.append(i)
            lll.append(j) 
for i in range(n):
    for j in range(m):
        for k in ll:
            l[k][j]=0
        for k in lll:
            l[i][k]=0
for i in l:
    print(*i) 