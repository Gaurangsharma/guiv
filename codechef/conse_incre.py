n=[int(i) for i in input()]
l=[]
for i in range(len(n)-1):
    j=i
    while( j<(len(n)-1) and n[j+1]>n[j]):
        j+=1
    l.append([sum(n[i:j+1]),n[i],len(n[i:j+1])])
l.append([n[-1],1])
sm_max=max(l)
sm_max_index=n.index(sm_max[1])
print(sm_max[0],":",sm_max_index+1,"-",sm_max_index+sm_max[2],sep="")