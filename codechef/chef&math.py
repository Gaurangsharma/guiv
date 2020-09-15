k=1
for _ in range(int(input())):
    n=list(input())
    for i in range(int(input())):
        num,char=map(str,input().split())
        if(i==0):
            print("Test case : ",k)
        ans=0
        if(char=="+"):
            for j in range(len(n)):
                ans+=int(n[j])+int(num)
                n[j]=str(int(n[j])+int(num))
            print(ans)
        elif(char=="*"):
            for j in range(len(n)):
                ans+=int(n[j])*int(num)
            print(ans)
        else:
            if(num=='0'):
                print("INVALID INPUT.'0' IS EVIL")
            else:
                for j in range(len(n)):
                    ans+=int(n[j])//int(num)
                print(ans)
            
    k+=1