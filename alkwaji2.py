from math import sqrt
def nod(n):
    cnt = 0
    for i in range(1, (int)(sqrt(n)) + 1) : 
        if (n % i == 0) :  
            if (n / i == i) : 
                cnt = cnt + 1
            else : 
                cnt = cnt + 2 
    return cnt 
ll=[]
for i in range(int(input())):
    ll.append(list(map(int,input().split()))) 
for i in range(int(input())):
    l,r,k=list(map(int,input().split()))
    ww=[]  
    s=0
    for i in range(len(ll)): 
        if ll[i][0]<=r and ll[i][0]>=l:
            ww.append(ll[i]) 
    for j in range(len(ww)):
        factor=nod(ww[j][1])
        print(factor)
        s^=factor
    if s <k:
        print(s)
    else:
        print(0)