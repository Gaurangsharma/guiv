n,k=map(int,input().split())
l=list(map(int,input().split()))
ll=[]
lll=[]
for i in l:
    ll.append(k-i)
ll.sort(reverse=True)
ll.remove(0) 
for i in range(len(ll)):
    lll.append(k-ll[i])
for i in range(3):
    print(lll[i],end=' ') 
    