l=list("WELCOMETOGUVICORPORATIONS") 
n=list(input())
ll,lll=[],[]
for j in range(0,len(l),5):
    ll.append(l[j:j+5])
k=0
for i in range(len(ll)):
    for j in range(len(ll[i])):
        if k==len(n):
            break 
        if ll[i][j]==n[k]: 
            lll.append([i,j])
            k+=1   
if k==len(n):   
    print(*lll[0])
    print(*lll[-1])
else:print(0)