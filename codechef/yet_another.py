for _ in range(int(input())):
    n,k=list(map(int,input().split()))
    l=list(map(int,input().split()))
    ans=0
    for i in range(n):
        ans=k%l[i]
    print(ans)