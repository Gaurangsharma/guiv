n=int(input())
l=list(map(int,input().split()))
ll=[]
for i in l:
    if l.count(i)>1:
        ll.append(i)
if ll==[]:
    print("unique")
else:
    print(ll[0])
