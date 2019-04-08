n=int(input())
l=list(map(int,input().split()))   
m=sum(l)
llll=[]
for i in range(len(l)):
    ll=[]
    for j in range(i,len(l)):
        k=[i,j]
        ll.append(k) 
    for j in range(len(ll)): 
        s=sum(l[ll[j][0]:ll[j][1]+1])
        lee=len(l[ll[j][0]:ll[j][1]+1])
        if len(l)-lee != 0:
            if (s/lee)>((m-s)/(len(l)-lee)): 
                lll=[ll[j][0]+1,ll[j][1]+1] 
                llll.append(lll)
        else:
            if m-s==0:
                lll=[ll[j][0]+1,ll[j][1]+1] 
                llll.append(lll)
print(len(llll))
for i in llll:
    print(*i)