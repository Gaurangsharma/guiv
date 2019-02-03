l=list(input())
c=0
ll=[]
n=len(l)
l.append('kdfhk')
for i in range(n):
    if l[i]=='a':
        if l[i+1]=='b':
            c+=1
        if l[i+1]=='a':  
            c+=1
            ll.append(c)
            c=0
        else:
            ll.append(c)
            c=0

        
    if l[i]=='b': 
        if l[i+1]=='a':
            c+=1 
            if l[i-1]=='b':
                c=0
        if l[i+1]=='b':  
            c+=1
            ll.append(c) 
            c=0
        else:
            ll.append(c) 
            c=0

ll.append(c) 
print(max(ll))
