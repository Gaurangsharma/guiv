t=int(input())
if(t>=1 and t<=10**3):
    for _ in range(t):
        n=list(input())
        for i in range(len(n)):
            print(int(n[i])-2,sep="",end="")
        print()