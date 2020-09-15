def get_prime(a,b):
    prime=[True]*(b+1)
    prime[0],prime[1]=False,False
    k=a
    a=2
    while(a*a<=b):
        if(prime[a]==True):
            for i in range(a*a,b+1,a):
                prime[i]=False
        a+=1
    l=[]
    for i in range(k,len(prime)):
        if(prime[i]):
            l.append(i)
    return l
    


A=int(input())
B=int(input())
pri=get_prime(A,B)
first,last=A//2*B//2,A*B
for i in range(len(pri)):
    for j in range(i+1,len(pri)):
        x=pri[i]*pri[j]
        if(x>=first and x<=last):
            print(pri[i],",",pri[j],sep="")