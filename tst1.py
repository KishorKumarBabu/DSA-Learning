def counthv(l):
    h=0
    v=0
    for i in range(1,len(l)-1):
        if l[i]>l[i-1] and l[i]>l[i+1]:
            h+=1
        elif l[i]<l[i-1] and l[i]<l[i+1]:
            v+=1
    return [h,v]
l=[3, 1, 2, 3]
print(counthv(l))
