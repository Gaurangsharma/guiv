for i in range(int(input())):
    n,x=list(map(int,input().split()))
    ll=[x]
    l=list(input())
    for i in l:
        if i=='R':
            x+=1
            ll.append(x)
        else:
            x-=1
            ll.append(x) 
    print(len(set(ll)))

