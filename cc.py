# 2
# 9
# 1 1 1 2 2 2 3 3 3
# 2
# 1 1  
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    ll=l.copy()
    c,temp=0,0 
    for i in range(len(l)):
        for j in range(i,len(l)):
            if l[i]!=l[j]:
                temp=l[j]
                l[j]=l[i]
                l[i]=temp 
                break 
    for i in range(len(ll)):
        if ll[i]!=l[i]:
            c+=1
    if c==len(l):
        print("Yes")
        print(*l)
    else:
        print("No")
