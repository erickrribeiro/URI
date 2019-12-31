op = input()
# M =  [[i+j for j in range(12)] for i in range(12)]

total = 0
count = 0
n = 12
for i in range(n):
    for j in range(n):
        value = float(input())
        if i > j:
            if i + j < n -1:            
                # M[i][j] = value
                # print('\t', M[i][j], end=" ")
                # count += M[i][j]
                # total += 1
                count += value
                continue
            
#         print('\t', 0, end=" ")
#     print()
# print(total)

if op == "S":   
    print("{0:.1f}".format(count))
else:
    print("{0:.1f}".format(count/30))