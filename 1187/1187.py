op = input()
# M =  [[i+j for j in range(12)] for i in range(12)]

total = 0
count = 0
n = 12
for i in range(n):
    for j in range(n):
        value = float(input())
        if i + j < n -1:
            if i < j:
                # M[i][j] = value
                # print('\t', M[i][j], end=" ")
                # count += M[i][j]
                count += value
                continue
            
        # print('\t', 0, end=" ")
    # print()
# print(total, count)

if op == "S":   
    print("{0:.1f}".format(count))
else:
    print("{0:.1f}".format(count/30))