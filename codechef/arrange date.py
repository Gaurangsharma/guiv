n=int(input())
date,month,year=[],[],[]
for _ in range(n):
    dat,mont,yea=map(int,input().split('/'))
    date.append([dat,mont,yea])
date.sort(key=lambda x: x[0])
date.sort(key=lambda x: x[1])
date.sort(key=lambda x: x[2])
for i in date:
    print(i[0],"/",i[1],"/",i[2],sep="")