l1=input()
l2=input()
if l2 in l1:
    l1=list(l1)
    k=list(l2).pop(0)
    print(l1.index(k))
else:
    print("-1")