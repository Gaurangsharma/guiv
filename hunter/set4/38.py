def genbraces(n,l):
    ll=[] 
    print(l)
    if n==0:
        return l
    if l==[]:
        l=[['{','}']]
        ll=l.copy()
    else: 
        for i in range(len(l)):
            for j in range(0,len(i),2): 
                if j==0:
                    l[i].insert(0,'{')
                else:l[i].insert(j-1,'{')
                l[i].insert(j+2,'}')
                ll.append(l)  
    n-=1
    ll=set(*ll)
    ll=list(ll)
    genbraces(n,ll)

n=int(input()) 
l=[]
print(genbraces(n,l))