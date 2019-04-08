for _ in range(int(input())):
    n = int(input())
    l = input()
    wstt = ''
    for i in l:
        if i=='E':
            wstt+='S'
        else:
            wstt+='E'
    print('Case #'+str(_+1)+":",wstt)