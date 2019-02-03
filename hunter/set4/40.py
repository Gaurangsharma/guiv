def ispalendrom(n):
    l=list(n)
    ll=[]
    for i in l:
        ll.append(int(i))
    c=0 
    for i in range(len(ll)//2): 
        if ll[i]==ll[-(i+1)]:
            c+=1
    if c==len(l)//2:
        print("YES")
    else:
        print("No")
l=list(input())
ll=[]
for i in l:
    ll.append(int(i))
k=sum(ll)
ispalendrom(str(k))