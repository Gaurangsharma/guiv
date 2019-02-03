n=list(input())
l,ll=[],[]
l1,l2=[],[]
for i in range(len(n)):
    l=n[:i]+n[i+1:]
    ll.append(l)
for i in range(len(ll)):
    l=ll[i]
    for j in range(len(l)//2):
        l1.append(l[j])
    for k in range(j+1,len(l)):
        l2.append(l[k]) 
    if l1==l2:
        print("YES")
        break
    if i==len(n)-1:
        print("No")
    l1,l2=[],[]