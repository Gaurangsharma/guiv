# Input : 7
# 1 2 3 4 1 2 3
# Output :
# 4

n=int(input())
l=list(map(int,input().split()))
ll=[]
for i in l:
    if l.count(i)==1:
        ll.append(i)
for i in ll:
    print(i,end=" ")