# Input : 5 4
# 1 0 3 2 4
# 1 2 3 0
# Output :
# YES
p,q=map(int,input().split())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
c=0
if q<p:
    for i in m:
        if i in l:
            c+=1
    if c==q:
        print("YES")
    else:
        print("NO")
else:
    print("NO")        