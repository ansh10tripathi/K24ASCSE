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

# n= int(input("n:"))
# S = str(n)
# index = int(input("index:"))
# print("Value = ", S[index])
# S1 =S[0:index]
# S2 = S[index+1:]
# V = input("Value:")
# S = S1 +V+ S2
# print(S)

# S1 = input("S1:")
# S2 = input("S2:")
# res = True
# for x in S1:
#     if x not in S2:
#         res = False
# if res==True:
#     print("Scrembled")
# else:
#     print("Not scrambled")

# S1 = "WORLD"
# S2 = "HELLO"
# L = []
# for x in S1:
#     if x not in S2:
#         L.append(x)
# for x in S2:
#     if x not in S1:
#         L.append(x)
# S=""
# for x in L:
#     S=S+x 
# print(S)

# S = input("S:")
# L = len(S)
# R = ""
# for x in range(L-1,-1,-1):
#     R = R+S[x]
# print(R)

# S = input("S:")
# L =  []
# for x in S:
#     L.append(ord(x))
# L.sort(reverse=True)
# ST=""
# for x in L:
#     ST = ST+chr(x)
# print(ST)

# name = "Ansh Tripathi"
# index = name.index(' ')
# S1 = name[index+1 :]
# S2 = name[0:index]
# S = S1 + " "+ S2
# print(S)

n = int(input("enter the no. of rows:"))
for i in range(1,n+1):
    for j in range(i):
        print(i,end=' ')
    print()