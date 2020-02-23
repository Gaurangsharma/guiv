for _ in range(int(input())):
    l=list(map(int,input('')))
    l2=sorted(l)
    temp=False
    for i in range(len(l2)-1):
        if abs(l2[i]-l2[i+1])<=2:
            temp=True
            continue
        else:
            temp=False
            break
    if temp:
        print("YES")
    else:
        print("NO")

