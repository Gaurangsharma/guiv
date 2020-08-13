for _ in range(int(input())):
    n=int(input())
    l=[int(i) for i in input().split()]
    sm=sum(l)
    if(sm%n==0):
        print("Yes")
    else:
        print("No")