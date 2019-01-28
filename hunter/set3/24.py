from itertools import combinations
n,k=map(int,input().split())
l=list(map(int,input().split()))
ll=list(combinations(l,2))
for i in range(len(ll)): 
    if sum(ll[i])==k:
        print("YES")
        break 
    if len(ll)-1==i and sum(ll[i])!=k:
        print("No")