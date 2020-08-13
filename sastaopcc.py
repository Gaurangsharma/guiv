for _ in range(int(input())):
    arr1=[int(i) for i in input().split()]
    arr2=[int(i) for i in input().split()]
    count=0
    for i in range(3):
        if arr1[i]==arr2[i]:
            count+=1
    if(count==len(arr1)):
        print(-1)
    else:
        print(len(arr1)-count)