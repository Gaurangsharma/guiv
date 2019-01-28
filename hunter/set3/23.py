n,m=map(int,input().split())
l=[]
s=0
for i in range(n):
    l.append(list(map(int,input().split())))
i,j=0,0
while(i<n and j<m):
    if i==n-1 and j==m-1:
        break
    s+=l[i][j] 
    print(l[i][j])
    if i+1<n and j+1<m :
        if l[i+1][j]>l[i][j+1]:
            i+=1
        else:
            j+=1
    else:
        if i+1==n:
            j+=1
        if j+1==m:
            i+=1 
            
s+=l[n-1][m-1]
print(s)
