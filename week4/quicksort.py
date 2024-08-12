import sys
sys.setrecursionlimit(100000)
def sort(a,l,r):
    if r-l<=1:
        return()
    yellow=l+1
    for green in range(l+1,r):
        if a[green]<=a[l]:
            (a[yellow],a[green])=(a[green],a[yellow])
            yellow+=1
    (a[l],a[yellow-1])=(a[yellow-1],a[l])
    sort(a,l,yellow-1)
    sort(a,yellow,r)
    return(a)
a=list(range(10000,1,-1))
print(sort(a,0,len(a)))