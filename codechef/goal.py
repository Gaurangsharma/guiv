for _ in range(int(input())):
    n=int(input())  #n initially
    goals=list(input())
    win_point=(n//2)+1
    count=0
    k=False
    team_A,team_B=0,0
    for i in range(len(goals)):
        if i%2==0:
            if goals[i]=='1':
                team_A+=1
        else:
            if goals[i]=='1':
                team_B+=1
        if team_A==team_B:
            if team_A>=win_point:
                print(i+2)
                k=True
                break
            if team_B>=win_point:
                print(i+1)
                k=True
                break
    if k==False:
        print(len(goals))   #n ended