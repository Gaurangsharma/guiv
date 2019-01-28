l=list(input())
n,m=l.count('a'),l.count('b')
while(n!=m):
    l.pop()
    n,m=l.count('a'),l.count('b')
print(*l,sep='')