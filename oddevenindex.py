# Input : 5
# 1 0 3 2 4
# Output :
# 1 0 3 2 
n=int(input())
l=list(map(int,input().split()))
ll=[]
for i in range(len(l)):
    if i%2!=0 and l[i]%2==0:
        ll.append(l[i])
    if i%2==0 and l[i]%2!=0:
        ll.append(l[i])
for i in ll:
    print(i,end=" ")