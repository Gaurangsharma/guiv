# Input : 5
# 0 0 1 4 3
# Output :
# 43100 
n=int(input())
l=list(map(int,input().split()))
l.sort()
l.reverse()
for i in l:
    print(i,end="")