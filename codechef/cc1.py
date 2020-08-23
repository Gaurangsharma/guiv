T=int(input())
if(T>=1 and T<=100):
    for _ in range(T):
        n,k=list(map(int,input().split()))
        l=list(map(int,input().split()))
        count=1
        s=0
        m=max(l)
        if(k>=m):
            for i in range(len(l)):
                if((s+l[i])<=k):
                    s+=l[i]
                else:
                    count+=1
                    s=l[i]
            
            print(count)

        else:
            print(-1)
            
