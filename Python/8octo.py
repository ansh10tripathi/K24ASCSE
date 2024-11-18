
S = input("Enter a string: ")
# R = ""
# for x in S:
#     a = ord(x)
#     if a >=65 & a <=90:
#         a += 32
#         R += chr(a)
#     elif a >= 97 & a<= 122:
#         a-=32
#         R += chr(a)
#     else:
#         R += x
# print(R)
        
C = ""
D = ""
K = 3
for x in S:
    if ord(x)!=32:
        a=ord(x)
        if a >=65 & a<=90:
            a += K
            if a  > 90:
                 a = a -90+65-1
                 C+= chr(a)
            else:
                C= C+chr(a)
        else:
            a +=K
            if a >122:
                a=a-122+97-1
                C = C+chr(a)
            else:
                C =C+chr(a)
        
    else:
        C =  C+x
print("Encryption",C)
for x in C:
    if ord(x)!=32:
        a = ord(x)
        if a>=65 and a<=90:
            a-=K
            if a<65:
                a=a+90-65+1
                D=C+chr(a)
            else:
                D+=chr(a)
        else:
            a-=K
            if a<97:
                a=a+122-97+1
                D+=chr(a)
            else:
                D+=chr(a)
    else:
        D+=x
print("Decryption",D)
    
