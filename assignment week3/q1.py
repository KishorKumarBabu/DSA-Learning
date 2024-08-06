def contracting(l):
    lst=[]
    for i in range(len(l) - 1):
        diff=abs(l[i] - l[i + 1])
        lst.append(diff)
    for i in range(1,len(lst)):
        if lst[i -1]<=lst[i]:
            return False
    return True
l = [10, 7, 4, 1]
print(contracting(l)) 
        
        