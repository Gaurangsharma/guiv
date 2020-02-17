#fx=(x^2+bx+c)/sinx
# import math

# for _ in range(int(input())):
#     a,b,c,d=list(map(int,input().split()))
#     count=0
#     while(a!=b and count!=10000):
#         if a<b:
#             if c<d:
#                 a+=d
#                 b+=c
#             else:
#                 a+=c
#                 b+=d
#             if a==b:
#                 print("YES")
#                 break
#         else:
#             if c<d:
#                 a+=c
#                 b+=d
#             else:
#                 a+=d
#                 b+=c
#             if a==b:
#                 print("YES")
#                 break
#         count+=1
#     if count==10000:
#         print("NO")


for _ in range(int(input())):
    a,b,c,d=list(map(int,input().split()))
    if a==b:
        print("YES")
    elif(c==d):
        print("NO")
    else:
        if(abs(a-b)%abs(c-d)==0):
            print("YES")
        else:
            print("NO")




















    # fx=[]
    # for x in range(1,91,0.5):
    #     k=(x^2+b*x+c)/math.sin(x)
    #     if k>0:
    #         fx.append(k)
    # print(fx)
    # print(min(fx))
