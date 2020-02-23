n,rupee=map(int,input().split())
l=list(map(int,input().split()))
l2=sorted(l)
count=0
if l2[0]<rupee:
    count+=1
    rupee-=l2[0]
    for i in range(len(l2)-1):
        
        if rupee>l2[i+1]:
            count+=1
            rupee-=l2[i+1]
        else:
            break
    if (i+1)==(len(l2)-1):
        if rupee>l2[i+1]:
            count+=1
            rupee-=l2[i+1]
    print(count)
else:
    print(count)