n=int(input())
l=list(map(int,input().split()))
ll=[]
k=len(l)
for i in range(1,k+1):
    if n*i in l:
        ll.append(l[i-1])
print(len(ll))