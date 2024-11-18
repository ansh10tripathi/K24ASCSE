f = open("xyz.txt","r")
g = open("K24AT","w")
for x in f:
    g.write(x)
g.close()
f.close()