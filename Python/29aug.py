#TOTAL NO OF UPPER CASE LETTER LOWER CASE CHARACTER DEGIT SPECIAL CHAR
#A - Z 65-90  a-z 92-122  1-9 48 - 57
a = input("Enter the string:")
U = 0
L = 0
D = 0 
S = 0 
for x in a:
  if ord(x)>=65 and ord(x)<=90:
    U = U+1
  elif ord(x)>=97 and ord(x)<=122:
    L=L+1
  elif ord(x)>=48 and ord(x)<=57:
    D= D+1
  else:
    S=S+1
print("Total upper case letters:",U)
print("Total lower case letters:",L)
print("Total digit are:",D)
print("Total specialcharacter:",S)