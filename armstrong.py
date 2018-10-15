l=input()
sum=0
for i in l:
    x=int(i)
    sum+=x*x*x
if sum==int(l):
    print("yes")
else:
    print("no")