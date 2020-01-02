n = int(input())

while(n != 0):
    M =  [[0 for j in range(n)] for i in range(n)]

    max_digit = 0
    for i in range(n):
        total = 2 ** i
        for j in range(n):
            M[i][j] = total
            max_digit = max(total, max_digit)
            total = total * 2
            
    num_max_digits = len(str( max_digit))
    for i in range(n):     
        format_expr = "{:"+str(num_max_digits) + "d}"
        print(" ".join(map(lambda x: format_expr.format(x), M[i])))   
    print()

    n = int(input())