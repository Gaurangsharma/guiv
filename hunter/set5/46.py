n=int(input())
l=list(map(int,input().split()))
ll,lll=[] ,[]
for i in range(1,len(l)):
    ll.append(abs(sum(l[:i])-sum(l[i:])))
    lll.append(abs(len(l[:i])-len(l[i:]))) 
print(lll[ll.index(min(ll))]) 