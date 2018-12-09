
n=int(input())
l=list(map(int,input().split()))
ll=[]
for i in l:
    if l.count(i)>1:
        ll.append(i)
lll=set(ll)
for i in lll:
    print(i,end=" ")

# Input : 4
# 1 2 3 2 1
# Output :
# 1 2