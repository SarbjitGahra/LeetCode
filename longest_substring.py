def longest_string(a,b):
    c = [[ 0 for i in range(len(a)) ] for j in range(len(b))]
    max =0
    for i in range (0,len(a)):
        for j in range(0,len(b)):
            if a[i]== b[j]:
                if i ==0 or j ==0:
                    c[i][j]=1
                else:
                    c[i][j]= c[i-1][j-1]+1
                    if c[i][j]>max:
                        max = c[i][j]
                        s =a[:i+1]
            else:
                c[i][j]=0
    return s
print longest_string('abab','baba')
