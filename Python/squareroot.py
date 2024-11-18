#import math as m
# R = lambda x:int(m.sqrt(x))
# print(R(16))

# R1 = lambda x:m.factorial(x)
# print(R1(8))


#write a program that return remainder without using operators

# R = lambda a,b:m.gcd(a,b)
# print(R(8,6))

# R = lambda a,b: int(m.fmod(a,b))
# print(R(10,7))

# R = lambda a,b: int(m.remainder(a,b))
# print(R(69,3))

# def check(n):
#     r=n & 1
#     if r==0:
#         print("Even")
#     else:
#         print("Odd")
# check(9)
# check(7)
# check(8)

# count = 0
# def prime(n):
#     global count
#     dc=0
#     for x in range(1,n+1):
#         if n%x==0:
#             dc=dc+1
#     if dc==1 or dc==2:
#         print(n)
#          count=count+1
# for m in range(1,101):
#     prime(m)
# print("Total Prime Numbers are:",count)

# A = [1,2,3,4,5,6,7,8,9,10]
# B = [2,3,6,7,9]
# R = lambda x: x in A,B
# print(R)

# S = input()
# L = S.split(",")
# NL = list(map(int,L))
# r = lambda x: 
    

# import colorsys
# import turtle

# t = turtle.Turtle()
# s = turtle.Screen()

# s.bgcolor('black')
# t.speed(0)

# n = int(input("N: "))
# h = 0

# for i in range(460):
#     c = colorsys.hsv_to_rgb(h,1,0.8)
#     h+=1/n
#     t.color(c)
#     t.left(145)

#     for j in range(5):
#         t.forward(300)
#         t.left(150)

n = int(input("N: "))
for i in range(n):
    p=1
    for j in range(i,n):
        print(p, end=' ')
        p+=1
    print()
     