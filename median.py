l=list(map(int,input().split()))
x=len(l)
if x%2==0:
    p=int(x/2)
    q=int((x/2)+1)
    print(l[p-1]," ",l[q-1])
else:
    q=int((x+1)/2)
    print(l[q-1])