from itertools import permutations
n=int(input())
l=['{','}']*n 
ll=[]
o=0
flag=0
for i in permutations(l,n*2):
    if i[-1]=='{':
        break
    if i[0]=='}':
        break
    for j in i:
        if j=='{':
            o+=1
        if j=='}':
            o-=1 
        if o<0:
            flag=1
        print(o,j,i)
        if flag==0:ll.append(i)
print(list(set(ll)))