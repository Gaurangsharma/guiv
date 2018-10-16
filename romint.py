def value(n):
    if n=="I":
        return 1
    if n=="V":
        return 5
    if n=="X":
        return 10
l=input() 
res = 0
i = 0  
while (i < len(l)): 
    s1 = value(l[i]) 
    if (i+1 < len(l)): 
        s2 = value(l[i+1]) 
        if (s1 >= s2):
            res = res + s1 
            i = i + 1
        else: 
            res = res + s2 - s1 
            i = i + 2
    else: 
        res = res + s1 
        i = i + 1
print(res)