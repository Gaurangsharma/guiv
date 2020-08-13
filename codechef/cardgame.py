from math import ceil
n=int(input())
if(n<=10**5):
    for _ in range(n):
        powc,powr=map(int,input().split())
        if(powc<=10**6 and powr<=10**6):
            countc,countr=0,0
            countc+=ceil(powc/9)
            countr+=ceil(powr/9)
            if(countr<=countc):
                print(1,countr)
            else:
                print(0,countc)

            