for i in range(int(input())):
    n,k=list(map(int,input().split())) 
    l=list(map(int,input().split()))
    if n>1 and n<=1000: 
        s=0
        ss=[]
        l=list(set(l))
        l.sort()
        ll=l.copy()
        for i in l:
            m=min(l)
            s+=m
            l.remove(m) 
            for j in l:
                m+=k 
                if m in l:
                    s+=m
                else:
                    ss.append(s)
                    s=0
                    break 
        print(max(ss)+1)