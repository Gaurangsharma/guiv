l=list(input())
k=len(l)
ll=[]
lll=[]
if k%2==0:
    for i in range(k//2):
        ll.append(l[i])
    ll.reverse()
    for j in range(i+1,len(l)):
        lll.append(l[j])
else:
    for i in range(k//2+1):
        ll.append(l[i])
    ll.reverse()
    for j in range(i,len(l)):
        lll.append(l[j]) 
if ll==lll:
    print("Yes")
else:
    print("No")