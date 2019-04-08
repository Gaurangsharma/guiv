def find(mylist,element):
    if len(mylist)==0:
        return 0
    else:
        left = 0;right = len(mylist)-1
        mid = (left+right)//2
        while left<=right:
            mid = (left+right)//2
            if mylist[mid]>element:
                right = mid-1
            elif mylist[mid]<element:
                left = mid+1
            else:
                break
        return mid

for _ in range(int(input())):
    n = int(input())
    heights = [int(i) for i in input().split()]
    indices = [int(i) for i in input().split()]
    s = []
    l = []
    for i in range(n):
        ind = find(s,heights[i])
        s.insert(ind,heights[i])
        if i>0 and s[ind]>s[ind+1]:
            s[ind],s[ind+1]=s[ind+1],s[ind]
        l.append(s[indices[i]-1])
    print(*l)
    