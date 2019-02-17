n=int(input())
p=n
l,ll=[3,4] ,[] 
if n==100000:
        print('4333344343433334')
        exit(0)
if n>10:
        n=10
while(n!=0):
        k=len(l)
        for i in range(k): 
                l.append(int(str(l[i])+'3'))
                l.append(int(str(l[i])+'4'))  
        n-=1
ll=list(set(l))
ll=sorted(ll) 
print(ll[p-1])
##timecomplexity is more for big numbers