def max_subsequence(l):
    max=[]
    for i in range(len(l)):
        max.append(max(l[i:]))


for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
