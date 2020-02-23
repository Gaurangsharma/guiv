import math
def isPerfect(n):
    sq=math.sqrt(n)
    return (sq-math.floor(sq)==0)

n=int(input())
arr=list(map(int,input().split()))
q=int(input())
for __ in range(q):
    typ,arg1,arg2=map(int,input().split())
    if typ==1:
        prod=1
        left,r=arg1,arg2
        l=arr[(left-1):r]
        prod=int(math.exp(sum(map(math.log, l))))
        if isPerfect(prod):
            print("YES")
        else:
            print("NO")
    else:
        i,val=arg1,arg2
        print(arr[i]*i*val)