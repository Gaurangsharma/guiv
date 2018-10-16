n,k=list(map(int,input().split()))
l=list(map(int,input().split()))
print(l)
for i in range(k-1):
    l.remove(min(l))
print(l)
print(min(l))
