n=int(input())
l=list(map(int,input().split()))
ll=[]
p=1
for i in range(len(l)):
    p*=l[i]
for i in range(len(l)):
    print(p//l[i],end=' ')
