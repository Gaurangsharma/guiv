n=int(input())
l=list(map(int,input().split()))
ll=[]
l.reverse()
for i in l:
    ll.append(i)
    ll.append("->")
for i in range(len(ll)-1):
    print(ll[i],sep='',end='')
