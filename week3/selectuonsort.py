def selection(l):
    for i in range(len(l)):
        min=i
        for j in range(i,len(l)):
            if l[j] < l[min]:
                min=j
        l[i],l[min]=l[min],l[i]
    print(l)
l=list(range(000,1,-1))
selection(l)               