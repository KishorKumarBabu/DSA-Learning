
def merge(a,b):
    (c,m,n)=([],len(a),len(b))
    (i,j)=(0,0)
    while i+j < m+n:
        if i==m or a[i]>=b[j]:
            c.append(b[j])
            j=j+1
        elif j==n or a[i]<=b[j]:
            c.append(a[i])
            i=i+1
    print(c)
a=list(range(1,5,2))
b=list(range(0,5,2))    
merge(a,b)