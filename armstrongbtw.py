n,m=list(map(int,input().split()))
sum=0
for i in range(n+1,m):
    l=str(i)
    for j in l:
        x=int(j)
        sum+=x*x*x
    if sum==int(l):
        print(l,end=" ")
