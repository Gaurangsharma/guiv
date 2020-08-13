# n=int(input())
# l=[int(i) for i in input().split()]
# ans=[]
# if n<3:
#     print("NO")
#     exit(0)
# l.sort()
# for i in range(n-2):
#     if l[i+2]<(l[i+1]+l[i]):
#         ans.append([l[i+2],l[i+1],l[i]])
# if(len(ans)):
#     print("YES")
#     print(*max(ans))
# else:
#     print("NO")

# l=['a','b']
# l+='cd'
# print(l)

def getSum(x,arr,k):
    s=0
    for i in arr:
        s+=abs((x-i)**k)
    return s


n,k=map(int,input().split())
arr=list(map(int,input().split()))
start,end=min(arr),max(arr)
ans_dict={}
while(start<=end):
    mid=(start+end)//2
    mid_prev=mid-1
    mid_next=mid+1
    if(mid not in ans_dict):
        ans_dict[mid]=getSum(mid,arr,k)
    if(mid_prev not in ans_dict):
        ans_dict[mid_prev]=getSum(mid_prev,arr,k)
    if(mid_next not in ans_dict):
        ans_dict[mid_next]=getSum(mid_next,arr,k)
    if(ans_dict[mid_next]>ans_dict[mid] and ans_dict[mid_prev]>ans_dict[mid]):
        print(mid)
        exit(0)
    elif(ans_dict[mid_next]<ans_dict[mid]):
        start=mid
    else:
        end=mid