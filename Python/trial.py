S = 0
n = int(input())
x = 1
c = 1
while(c<=n):
  if(x%2!=0):
    S = S+x
  x= x+1
  c = c+1
print(S)
