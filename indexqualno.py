# Input : 8
# 8 7 6 8 4 7 8 7
# Output :
# 4 7
n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)):
    if l[i]==i:
        print(i,end=" ")