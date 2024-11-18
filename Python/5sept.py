def factorial(n):
    f = 1
    for x in range(1,n+1):
        f=f*x
    return f
r = factorial(10)
print("Factorial",r)