# S = "10,20,30,40,50,6,70,80,90,20,10,50,70"
# S1=""
# L = S.split(',')
# print(L)
# NL = list(map(int,L))
# print(NL)
# UL = []
# for x in NL:
#     if x not in UL:
#         UL.append(x)
# print(UL)
# for x in UL:
#     S1 = S1+str(x)+" "
# print(S1[0:-1])``

# S = input()
# UL=[]
# S1=""
# for x in S:
#     if x not in UL:
#         UL.append(x)
# print(UL)
# for x in UL:
#     S1 = S1+x+" "
# print(S1)

# S = "2,19,34,16,43,22,17,41,56,67,39,97,53"
# def prime(n):
#     dc=0
#     for x in range(1,n+1):
#         if n%x==0:
#             dc=dc+1
#     if dc==1 or dc==2:
#         return n
# L = S.split(',')
# NL = list(map(int,L))
# UL = list(filter(prime,NL))
# UL.sort(reverse=True)
# print(UL)

# S = "2,19,34,16,43,22,17,41,56,67,39,97,53"
# count_even = 0
# count_odd = 0
# L = list(map(int,input().split(',')))
# for x in L:
#     if x % 2==0:
#         count_even+=1
#     else:
#         count_odd+=1
# print(L)
# print("Even: ",count_even)
# print("Odd: ",count_odd)


# A=int(input("A: "))
# S=(A%10)+(A//10)
# if S<=9:
#     print(A)
# else:
#     print("Invalid")


# A = int(input("Dayb number:"))
# if A==1:
#     print("Sunday")
# elif A==2:
#     print("Monday")
# elif A==3:
#     print("Tuesday")
# elif A==4:
#     print("Wednsday")
# elif A==5:
#     print("Thrusday")
# elif A==6:
#     print("Friday")
# elif A==7:
#     print("Saturday")
# else:
#     print("invalid")
# A = int(input("Month number:"))
# if A==1 or A==3 or A==5 or A==7 or A==8 or A==10 or A==12:
#     print("31")
# elif A==2:
#     prine("28")
# else:
#     print("invalid")

# n = int(input("N: "))
# for x in range(1,n+1,2):
#     if n%x==0:
#         print(x)


# n = int(input())
# l = len(str(n))
# s =0 
# for x in str(n):
#     s = s+int(x)**l
# if s==n:
#     print("Amstrong")
# else:
#     print("not amstrong")

# n=int(input())
# l=len(str(n))
# org=n
# total=0
# while n!=0:
#   r=n%10
#   total=total+r**l
#   n=n//10
# if org==total:
#   print("armstrong")
# else:
#   print("not armstrong")

s= input()
c = input()
index = s.find(c)
if index==-1:
    pass
else:
    print(index)