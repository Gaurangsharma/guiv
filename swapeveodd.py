n=input()
for i in range(0,len(n),2):
    a=n[i]
    b=n[i+1]
    a,b=b,a
    print(a+b,end="")