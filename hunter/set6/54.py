n=int(input())
l=list(map(str,input().split()))
ll=[]
for i in range(len(l)):
    ll.append(l[i])
    print(min(ll),sep='',end=' ')

