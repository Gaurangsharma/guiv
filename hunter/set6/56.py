from itertools import combinations
n=list(map(int,input().split()))
l=list(map(int,input().split()))
ll,lll=[],[]
for i in combinations(l,2):
    ll.append(abs(sum(list(i))))
    lll.append(list(i)) 
print(*lll[ll.index(min(ll))])