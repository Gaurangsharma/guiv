s,k=list(map(str,input().split()))
s=list(s)
print(s,k)
for i in range(0,len(s)):
    if len(s[i:i+int(k)])==int(k):
        print(*s[i:i+int(k)],sep='',end=' ')