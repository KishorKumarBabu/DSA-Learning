def intreverse(n):
    r=0
    while n!=0:
        r=r*10+n%10
        n=n//10
    return r
print(intreverse(678))
