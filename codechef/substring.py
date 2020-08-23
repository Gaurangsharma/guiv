from itertools import permutations


def issubsequence(str1,str2,m,n):
    if( m==0 ):
        return True
    if( n==0 ):
        return False
    if(str1[m-1]== str2[n-1]):
        return issubsequence(str1,str2,m-1,n-1)
    return issubsequence(str1,str2,m,n-1)


t=int(input())
if (t<=10):
    for _ in range(t):
        str2=input()
        inpi,inpj=map(int,input().split())
        n=int(input())
        nl=len(str2)
        for __ in range(n):
            ansi,ansj=map(int,input().split())
            inpansi,inpansj="",""
            while(not(inpi==ansi and inpj==ansj)):
                if(inpi<ansi):
                    inpansi="".join("R"*(ansi-inpi))
                    inpi+=(ansi-inpi)
                else:
                    inpansi="".join("L"*(inpi-ansi))
                    inpi-=(inpi-ansi)
                if(inpj<ansj):
                    inpansj="".join("U"*(ansj-inpj))
                    inpj+=(ansj-inpj)
                else:
                    inpansj="".join("D"*(inpj-ansj))
                    inpj-=(inpj-ansj)
            l=[]
            for i in permutations(inpansi+inpansj):
                k=list(i)
                str1="".join(k)
                ml=len(str1)
            
                if(issubsequence(str1,str2,ml,nl)):
                    l.append(ml)
            if(len(l)>0):
                print("Yes",min(l))
            else:
                print("No")
            
            
                