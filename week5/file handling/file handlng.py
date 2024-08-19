f=open("input.txt","r")
c=f.read()
for line in c:
    d=line.split()
print(d)
f.close()