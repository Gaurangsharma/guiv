import re
l=list(input())
num,alp=0,''
for i in range(len(l)):
    if re.match('\D', l[i]): 
        alp=l[i]
    else: 
        num=num*10+int(l[i])  
    if i!=len(l)-1:
        if re.match('\D', l[i+1]):
            if num%2==0:
                print(alp*num,end='')
            else:print(alp,num,sep='',end='')
            num,alp=0,''
    else:
        if num%2==0:
            print(alp*num,end='')
        else:
            print(alp,num,sep='',end='')