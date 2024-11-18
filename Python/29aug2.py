S = input("Enter String in Upper Case:")
S1=""
for x in S:
    a = ord(x)+32
    S1 = S1+chr(a)
print("String in Lower Case:",S1)
