t=int(input())
if(t<=100):
    for _ in range(t):
        n=list(input())
        print("Test case: "+str(_+1))
        for i in range(int(input())):
            status=False
            a=list(input())
            num,char=a[0],a[1]
            if(char=="*"):
                ans=0
                for j in range(len(n)):
                    ans+=int(n[j])*int(num)
                print(ans)
            if(char=="/"):
                ans=0
                for j in range(len(n)):
                    if(num!='0'):
                        ans+=int(int(n[j])/int(num))
                    else:
                        status=True
                        break
                if(status):
                    print("INVALID INPUT.'0' IS EVIL")
                else:
                    print(ans)
            if(char=="+"):
                ans=0
                for j in range(len(n)):
                    ans+=int(n[j])+int(num)
                    n[j]=int(n[j])+int(num)
                print(ans)