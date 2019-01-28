def isprime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):
            return False    

    return True
a,b=map(int,input().split())
l=[]
c=0

for i in range(a,b+1): 
    if isprime(bin(i).count('1')):
        c+=1
print(c)