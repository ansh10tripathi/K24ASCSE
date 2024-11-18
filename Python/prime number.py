count = 0
def prime(n):
    global count
    dc=0
    for x in range(1,n+1):
        if n%x==0:
            dc=dc+1
    if dc==1 or dc==2:
        print(n)
        count=count+1
a = int(input("First Number: "))
b = int(input("Second Number: "))
for m in range(a,b+1):
    prime(m)
print("Total Prime Numbers are:",count)
