n=list(input())
for i in range(len(n)-1): 
    if ord(n[i])==32 and ord(n[i+1])==32:
        n.pop(i)
print(*n,sep='')