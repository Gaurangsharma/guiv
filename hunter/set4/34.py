from itertools import permutations
n= input() 
nn=list(n) 
k=''
ll=[]
l=list(permutations(n,len(nn))) 
for i in range(len(l)): 
    k=''.join(l[i])
    ll.append(k) 
ll.sort()
for i in range(len(ll)): 
    if int(ll[i]) == int(n):
        break
if i==len(ll)-1:
    print("impossible")
else:print(ll[i+1])