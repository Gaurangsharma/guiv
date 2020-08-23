T=int(input())
if(T>=1 and T<=100):
    for _ in range(T):
        n,k=list(map(int,input().split()))
        l=list(input())
        c_0,c_1=l.count('0'),l.count('1')
        div=n//k
        base=""
        for i in range(k):
            if(i%2==0):
                base+="".join("0")
            else:
                base+="".join("1")
        rev=base
        while(div>1):
            new="".join(reversed(rev))
            base+="".join(new)
            rev=new
            div-=1
        i_0,i_1=base.count('0'),base.count('1')
        if(i_0==c_0 and i_1==c_1):
            print(base)
        else:
            print("IMPOSSIBLE")