n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
i,j=0,0
min_way=0
new_n=n
count=0
while(count>=(n*n)):
    l=[]
    ini_i,ini_j=i,ini_j
    if i<new_n and j<new_n and i>=0 and j>=0:
        while(j<n):
            print(arr[i][j],"1")
            count+=1
            l.append(arr[i][j])
            j+=1
        while(i<n):
            print(arr[i][j],"2")
            count+=1
            l.append(arr[i][j])
            i+=1
        while(i>0):
            print(arr[i][j],"3")
            count+=1
            l.append(arr[i][j])
            i-=1
        while(j>0):
            print(arr[i][j],"4")
            count+=1
            l.append(arr[i][j])
            j-=1
        new_n-=1  
    print(l)
        
            