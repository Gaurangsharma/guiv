for _ in range(int(input())):
    m,n=list(map(int,input().split()))
    arr=[]
    ma=0
    for i in range(1,m*n):
        if(m*n)%(i*i)==0:
            if ma<i:
                ma=i
    print((m*n)//(ma*ma))
            