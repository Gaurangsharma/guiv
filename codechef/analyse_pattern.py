t=int(input())
if(t<=10**2):
    for _ in range(t):
        n=int(input())
        l=[["S"],['S','S'],['S','S','E'],['S','S','E','C'],['S','S','E'],['S','S'],['S']]
        for i in l[(n)%7-1]: 
            k=ord(i) 
            print(k,end=" ")
        print()