n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)):
    if l[i]==i:
        print(i,end=" ")
