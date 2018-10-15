l=input()
c=0
for i in l:
    if i=="@"or i=="!"or i=="$"or i=="%"or i=="^" or i=="#"or i=="*" or i=="("or i=="&" or i==")"or i=="-" or i=="+":
        c+=1
print(c)