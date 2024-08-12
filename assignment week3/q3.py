def leftrotate(l):
    n=len(l)
    rotate=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotate[n-j-1][i]=l[i][j]
    return rotate
print(leftrotate([[1,2],[3,4]]))