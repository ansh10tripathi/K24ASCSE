n = int(input())

even_factors = []
for i in range(1,n+1):
    if n%i==0 and i%2==0:
      even_factors.append(i)
if even_factors:
      print(" ".join(map(str,even_factors)))
else:
   print(-1)
