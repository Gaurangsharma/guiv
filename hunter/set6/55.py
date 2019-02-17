n,k=list(map(int,input().split()))
l=list(map(int,input().split()))
ll=[]
while(k!=0):
    for i in range(len(l)):
        if i==len(l)-1:
            ll.append(l[0])
        else:ll.append(l[i+1]) 
    l=ll.copy() 
    ll=[]
    k-=1
print(*l)