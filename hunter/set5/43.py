l=list(input())
i=0
c=''
d=''
while(i<len(l)-1): 
    if ord(l[i])>97 and ord(l[i])<122:
        c=''.join(l[i])
    if ord(l[i])>48 and ord(l[i])<57:
        d+=''.join(l[i])
    print(c,d)
    if ord(l[i+1])>97 and ord(l[i+1])<122:
        print(c*int(d),end='')
        i+=1 
    else:
        i+=1