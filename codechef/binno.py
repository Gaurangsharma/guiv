def decimalToBinary(N): 
      
    # To store the binary number  
    B_Number = 0
    cnt = 0
    while (N != 0): 
        rem = N % 2
        c = pow(10, cnt)  
        B_Number += rem * c  
        N //= 2
          
        # Count used to store exponent value  
        cnt += 1
      
    return B_Number  
for _ in range(int(input())):
    n=int(input())
    ans=0
    l=list(str(decimalToBinary(n)))
    rev=l[::-1]
    for i in range(len(rev)):
        if rev[i]=='1':
            ans+=i
    print(ans)
