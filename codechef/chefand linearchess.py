n=int(input())
if(n<=100):
    for _ in range(n):
        no_player,k_chef=map(int,input().split())
        players=list(map(int,input().split()))
        if(no_player<=10**3 and k_chef<=10**9 and len(players)<=10**9):
            valid_player=[]
            for i in range(no_player):
                if(players[i]<=k_chef and k_chef%players[i]==0):
                    valid_player.append(k_chef-players[i])
            valid_player.sort()
            if(len(valid_player)>0):
                print(k_chef-valid_player[0])
            else:
                print(-1)
