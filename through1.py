from collections import Counter 
n=int(input())
l=list(input())
ll=[]
print(l)
for i in range(len(l)):
    lll=[l[:i+1],l[i:]]
    ll.append(lll)
print(Counter(ll[0][1]))

# k=int(input())
# s=input()
# count,c,s1,sk=0,0,'',''
# for i in range(2,len(s)-2):
#     if s[i-1]==s[i]:
#         c+=1
# print(c)