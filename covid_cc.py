check_name=["ACov","BCov","CCov","DCov","ECov","FCov"]
check_letter=["A","B","C","D","E","F"]
name=[]
letter=[]
stack_name=[]
stack_letter=[]
main=[]
score=0
for _ in range(6):
    k=input()
    if(_!=5):
        input()
    main.append(k)
    k=list(k)
    name.append(k[-4::-1])
    letter.append(k[-2])
for i in range(len(name)):
    # n=i[-1:len(i)-1,:-1]
    name[i].reverse()
    s="".join(name[i])
    if(s in check_name and s not in stack_name):
        score+=0.5
        stack_name.append(s)
    k=name[i][0]
    if(letter[i] not in stack_letter and letter[i]==k):
        score+=0.5
        stack_letter.append(letter[i])
print(score,"out of 6")