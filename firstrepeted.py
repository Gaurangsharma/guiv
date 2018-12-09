n=int(input())
l=list(map(int,input().split()))
ll=[]
for i in l:
    if l.count(i)>1:
        ll.append(i)
print(ll[0])
