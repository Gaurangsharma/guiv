n,k=list(map(int,input().split()))
l=list(map(int,input().split()))
ll=[]
for i in range(n):
    if i%2!=0:
        ll.append(i)
print(l[k-1])