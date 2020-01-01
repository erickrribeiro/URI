import math

n = int(input())

while(n != 0):
    M =  [[0 for j in range(n)] for i in range(n)]

    x = n
    count = 1
    ofset = 0
    while ofset < n:        
        for i in range(n - ofset):
            M[i + ofset][i] = count
            M[i][i+ofset] = count

        count += 1
        ofset += 1

    for i in range(n):     
        print(" ".join(map(lambda x: "{:3d}".format(x), M[i])))   
    print()

    n = int(input())

#    0  1  2 3
# 0 00 01 02 03
# 1 10 11 12 13
# 2 20 21 22 14
# 3 30 31 32 33