n=int(input())
l=list(map(int,input().split())) 
ll=[]
s=0
if max(l)<0:
    print(max(l))
if min(l)>0:
    print(sum(l))
if min(l)<0 and max(l)>0:
    for i in range(len(l)):
        for j in range(i,len(l)):
            s+=l[j]
            ll.append(s)
        s=0
    print(max(ll))