n,q=list(map(int,input().split()))
a=list(map(int,input().split()))
l=list(map(int,input().split()))
s=0
for _ in range(q):
    one,second=list(map(int,input().split()))
    for i in range(one-1,second):
        s+=a[i]*l[i]
    print(s)
    s=0

