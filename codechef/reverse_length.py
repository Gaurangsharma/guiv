n=int(input())
if(n>=0 and n<=10**6):
    n=str(n)
    n=list(int(i) for i in n)
    n_len=len(n)
    k=1
    temp=False
    while(n_len>=1):
        if(k==1):
            n=n[:n_len-1]
        if(k==2):
            if(n[-1]%2==0):
                n=n[:n_len-1]
            else:
                temp=True
                break
        if(k==3):
            if(sum(n)%3==0):
                n=n[:n_len-1]
            else:
                temp=True
                break
        if(k==4):
            dig=n[-1]+n[-2]*10
            if(dig%4==0):
                n=n[:n_len-1]
            else:
                temp=True
                break
        if(k==5):
            if(n[-1]==0 or n[-1]==5):
                n=n[:n_len-1]
            else:
                temp=True
                break
        if(k==6):
            if(sum(n)%6==0):
                n=n[:n_len-1]
            else:
                temp=True
                break
        k+=1    
        n_len-=1
    if(temp):
        print("No")
    else:
        print("Yes")
