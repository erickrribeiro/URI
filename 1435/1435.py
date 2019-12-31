import math

n = int(input())

while(n != 0):
    M =  [[0 for j in range(n)] for i in range(n)]    
    
    for q in range(math.ceil(n / 2)):
        for i in range(q, n-q):
            for j in range(q, n-q):
                M[i][j] += 1
    
    for i in range(n):     
        print(" ".join(map(lambda x: "{:3d}".format(x), M[i])))   
    print()
    n = int(input())
