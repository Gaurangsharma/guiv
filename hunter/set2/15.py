n=int(input())
l=list(map(int,input().split()))
ll=[]
m=max(l)
k=l.index(m)
ll.append(m)
for i in range(k+1,len(l)):
    max=i
    for j in range(i,len(l)): 
        if l[j]>max:
            max=l[j]
    if max==i:
        ll.append(l[i])
print(*ll)
print(m)