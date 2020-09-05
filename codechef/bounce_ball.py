t=int(input())
if(t<=10**5):
    for _ in range(t):
        n=int(input())
        bit=list(bin(n))
        print(bit)
        bounce=bit.count('1')
        print(bounce-1)