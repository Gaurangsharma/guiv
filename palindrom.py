l=list(input())
b=list(l)
l.reverse()
ll=[]
for i in l:
    p=i
    ll.append(p)
if ll==b:
    print("yes")
else:
    print("no")
