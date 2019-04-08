for _ in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    s,c=0,0
    l.sort()
    l=set(l)
    l1=[]
    for i in l:
        s=k+i
        l1.append(i)
        if s in l:
            l1.append(s) 
        else:
            l1.remove(i)
    l1=set(l1)
    print(l1)
    print(sum(l1)+1)