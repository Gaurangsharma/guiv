# Input : 5
# -1 2 0 -3 1
# Output :
# -1 1
n=int(input())
l=list(map(int,input().split()))
ll=[]
def add(i,j):return i+j
for i in range(0,len(l)):
    for j in l :
            if l[i]+j == 0 :
                print(l[i],"",j)
            break
