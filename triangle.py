for _ in range(int(input())):
    a,b,c=map(int,input().split())
    l=[a,b,c]
    m=max(l)
    l.remove(m)
    ans=list(map(lambda x:x**2,l))
    if m**2==sum(ans):
        print("YES")
    else:
        print("NO")