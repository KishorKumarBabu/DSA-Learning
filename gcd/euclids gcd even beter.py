#using recurtion
''' def gcd(m,n):
    if m<n:
        (m,n)=(n,m)
    if m%n==0:
        return n
    else:
        r=m%n
        return gcd(n,r)
print(gcd(14,63)) '''
#using loop
def gcd(m,n):
    if m<n:
        (m,n)=(n,m)
    while m%n!=0:
        r=m%n
        m,n=n,r
    return(n)
print(gcd(14,63))