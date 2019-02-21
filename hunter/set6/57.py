n=int(input())
l=list(map(int,input().split()))
ll,lll=[],[] 
for i in range(len(l)):
    c=0
    ll.append(l[i])
    if l[i]==max(ll):
        c+=1
        lll.append(c) 
    else:   
        k=0
        for p in range(l[i]+1,max(ll)+1):
            if p in ll:
                k=p
                break   
        print(k) 
        l[i],max(ll)
        for j in range(l[i],max(ll)): 
            if j in ll:  
                c+=1
        lll.append(c)  
    print(lll)