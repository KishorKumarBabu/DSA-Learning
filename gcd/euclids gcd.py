#using recurtion
''' def gcd(m,n):
    if m<n:
        (m,n)=(n,m)
    if m%n==0:
        return (n)
    else:
        diff=m-n
        return gcd(max(n,diff),min(n,diff))
print(gcd(14,63))'''
# using while
def gcd(m,n):
    if m<n:
        (m,n)=(n,m)
    while m%n!=0:
        diff=m-n
        m,n=max(n,diff),min(n,diff)
    return n
print(gcd(14,63))