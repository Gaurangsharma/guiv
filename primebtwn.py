l,m=list(map(int,input().split()))
c=0
for n in range(l+1,m):
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        print(n,"prime")

