n,m=list(map(int,input().split()))
inp=[]
for i in range(n):
    for j in input().split():
        inp.append(j)
out=[]
for k in range(n):
    for l in input().split():
        out.append(l)
inp_fill,out_fill=[],[]
for i in range(n):
    for j in range(m):
        if inp[i][j]=='#':
            inp_fill.append([i,j])
for i in range(len(inp)):
    for j in range(m):
        if out[i][j]=='#':
            out_fill.append([i,j])
print(inp_fill," ",out_fill)
if len(inp_fill)==len(out_fill):
    for i in range(len(inp)):
        