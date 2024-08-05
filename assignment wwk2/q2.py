def factors(n):
    fl=[]
    for i in range(1,n+1):
       if n%i==0:
            fl.append(i)
    return fl

def isprime(n):
    return (factors(n)==[1,n])

def sumprimes(l):
    sum=0
    for i in range(len(l)):
        if(isprime(l[i])):
            sum+=l[i]
    return(sum)
l=[23,46,3,457,8]
print(sumprimes(l))
