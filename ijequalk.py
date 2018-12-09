# Input : 5
# 1 2 1 3 4
# Output :
# 1 2 3
# 1 3 4
# 1 3 4
n=int(input())
l=list(map(int,input().split()))
ll=[]
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        for k in range(j+1,len(l)):
            if l[i]+l[j]==l[k]:
                print(l[i],"",l[j],"",l[k])
