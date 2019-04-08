from math import ceil, floor
for _ in range(int(input())):
    x = int(input())
    l ,r= list(str(x)),list(str(x)) 
    for i in range(len(l)):
        if l[i] == '7':
            l[i]='2'
            r[i]='5'
        elif l[i] == '8':
            l[i]='3'
            r[i]='5'
        elif l[i]=='9':
            l[i]='3'
            r[i]='6'
        elif l[i]=='6':
            l[i]='3'
            r[i]='3'
        elif l[i]=='5':
            l[i]='2'
            r[i]='3'
        elif l[i]=='4':
            l[i]='2'
            r[i]='2'
        elif l[i]=='3':
            l[i]='1'
            r[i]='2'
        elif l[i]=='2':
            l[i]='1'
            r[i]='1'
        elif l[i]=='1':
            l[i]='0'
            r[i]='1'

    print('Case #'+str(_+1)+":",int("".join(l)),int("".join(r[i])))