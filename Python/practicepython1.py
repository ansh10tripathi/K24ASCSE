#write a function that take integer n from user and check weather it is divisible by 3 and 4
def devisible(n):
    if n%3==0 and n%5==0:
        print(n,"divisible by 3 and 5")
    else:
        print("not divisible by 3 and5")
#return n
n =int(input())
devisible(n)


