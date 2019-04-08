from math import floor
n,k=map(int,input().split())
l=list(map(int,input().split()))
ans=0
while k!=0:
    m=max(l)
    l.remove(m)
    l.append(floor(m/2))
    ans+=m
    k-=1
print(ans % 1000000007)