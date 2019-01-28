n=int(input())
l=list(map(int,input().split()))
ll=[]
p=1
if min(l)>0:
    for i in range(len(l)):
        p*=l[i]
    print(p)
if max(l)<0:
    if len(l)%2==0:
        for i in range(len(l)):
            p*=l[i]
        print(p)
    else:
        if l[0]>l[-1]:
            l.pop()
            for i in range(len(l)):
                p*=l[i]
            print(p)
        else:
            l.pop(-1)
            for i in range(len(l)):
                p*=l[i]
            print(p)
if max(l)>0 and min(l)<0:
    for i in range(len(l)):
        for j in range(i,len(l)):
            p*=l[j]
            ll.append(p)
        p=1
    print(max(ll))
