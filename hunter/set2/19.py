n,k=map(int,input().split())
l=[]
ll=[]
for i in range(n):
    l.append(list(map(int,input().split())))
for i in range(n-1):
    ll.append(set(l[i]).intersection(set(l[i+1])))
print(*ll[-1])

    