S = input("String: ")
L=[]
for x in S:
    if x not in L:
        L.append(x)
print("Count of unique Character: ",len(L))
R=""
for x in L:
    R+=x
print("Unique String: ",R)
