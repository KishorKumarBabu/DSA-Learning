def square(x):
    return x*x
def iseven(x):
    return (x%2==0)
l=[square(x) for x in range(100) if iseven(x) ]
print(l)