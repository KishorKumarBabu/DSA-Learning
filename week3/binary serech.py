def binary(seq,v,r,l):
    if r-l == 0:
        return False
    mid=(r+l)//2
    if seq[mid] == v:
        return True
    if v<seq[mid]:
        return binary(seq,v,r,mid)
    else:
        return binary(seq,v,mid+1,l)
seq=[1,2,3,4,5,6,7,8,9]
r=0
l=len(seq)
v=int(input())
print(binary(seq,v,r,l))
    