from itertools import combinations 
n,k=list(map(int,input().split()))
l,ll=[],[] 
for i in range(1,n+1):
    l.append(i)
for j in combinations(l,k):
    ll.append(j)
print(len(ll))
