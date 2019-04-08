m = 10**9+7
n, q = map(int,input().split())
top = 1
left = n+1
right = n+1
bottom = 2**n
edges = (2**(n+1)-2)%m
for _ in range(q):
    w = [int(i) for i in input().split()]
    if len(w)==1:
        print(edges)
    else:
        t = w[1]
        if t==1 or t==2:
            top*=2
            bottom*=2
            edges = (edges*2 + right)%m
        elif t==3:
            edges = (edges*2 + top)%m
            right*=2
            left = right
            top = bottom
        else:
            edges = (edges*2 + bottom)%m
            right*=2
            left = right
            bottom = top