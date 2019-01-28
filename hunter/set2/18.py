n=int(input())
l=[]
ll=[]
lll=[i for i in range(n)] 
c=0
for i in range(n):
    l.append(list(map(int,input().split())))
for i in range(len(l)):
    ll.append(l[i].count(1)) 
if ll==lll:
    print("1")
else:   
    ll.reverse()
    if ll==lll:
        print("1")
    else:
        print("0")

    