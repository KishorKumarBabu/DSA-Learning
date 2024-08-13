l=[(x,y,z) for x in range(100) for y in range(x,100) for z in range(y,100) if x*x + y*y== z*z ]
print(l)