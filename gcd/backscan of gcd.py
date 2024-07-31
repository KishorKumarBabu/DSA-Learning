def gcd(m,n):
    for i in range(min(m,n)+1,1,-1):
        if m%i==0 and n%i==0:
            mrcf=i
            
            return(mrcf)
print(gcd(14,63))