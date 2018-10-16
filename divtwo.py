n=int(input())
for i in range(n):
    if n%2==0:
        n=int(n/2)
    else:
        break
    print(n)