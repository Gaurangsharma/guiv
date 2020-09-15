t=int(input())
if(t>=1 and t<=10**3):
    for _ in range(t):
        n=int(input())
        for i in str(n):
            print(int(i)-2,sep="",end="")
        print()