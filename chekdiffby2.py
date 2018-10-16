n,m=list(map(str,input().split()))
c=0
for i in range(len(n)):
    if n[i]!=m[i]:
        c+=1
if c==1:
    print("yes")
else:
    print("no")