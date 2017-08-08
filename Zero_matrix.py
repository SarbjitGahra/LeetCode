def setZero(a,r,c):
#make a list of size r and set it to zero
    rows=[0]*r
#make a list of size r and set it to zero
    cols=[0]*c
    for i in range(r):
        for j in range(c):
            if a[i][j]==1:
                rows[i]=1
                cols[j]=1
    for i in range(r):
        for j in range(c):
            if rows[i]==1 or cols==1:
                a[i][j]=1
    return a
print setZero([[0,0,1],[1,0,0],[0,0,0]],3,3)
