n,m=map(int,input().split())
s=0
if m>n:
    print('0')
else:
    for i in range(n//2):
        s+=m
        if s==n:
            print(i+1)
            break