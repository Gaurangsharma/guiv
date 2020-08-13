n=int(input())
if(n<=10**5):
    for _ in range(n):
        h,p=map(int,input().split())
        if(h<=10**6 and p<=10**5):
            if(p<(h//2)):
                print(0)
            elif(p>=h):
                print(1)
            else:
                while(p>0 and h>0):
                    h-=p
                    p//=2
                if(h<=0):
                    print(1)
                else:
                    print(0)
