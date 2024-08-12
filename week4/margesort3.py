def merge(a,b):
    (c,m,n)=([],len(a),len(b))
    (i,j)=(0,0)
    while i+j < m+n:
        if i==m:
            c.append(b[j])
            j=j+1
        elif j==n:
            c.append(a[i])
            i=i+1
        elif a[i]<=b[j]:
            c.append(a[i])
            i=i+1
        elif a[i]>=b[j]:
            c.append(b[j])
            j=i+1
    return c
a=list(range(1,5,2))
b=list(range(0,5,2))    
merge(a,b)
def sort(a,left,right):
    if right-left<=1:
        return (a[left:right])
    
    if right-left>1:
        mid=(left+right)//2
        l=sort(a,left,mid)
        r=sort(a,mid+1,right)
        return(merge(l,r))
a=list(range(1,10000,2))+list(range(0,10000,2))
print(sort(a,0,len(a)))