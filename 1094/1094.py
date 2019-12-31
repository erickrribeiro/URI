N = int(input())
statistic = { "R": 0, "S": 0, "C": 0 }
total = 0
while N > 0:
    q, t = input().split()
    q = int(q)
    statistic[t] += q
    total += q
    N -= 1

print("Total: {} cobaias".format(total))
print("Total de coelhos:", statistic["C"])
print("Total de ratos:", statistic["R"])
print("Total de sapos:", statistic["S"])
print("Percentual de coelhos: {0:.2f} %".format((statistic["C"] / total) * 100))
print("Percentual de ratos: {0:.2f} %".format((statistic["R"] / total) * 100))
print("Percentual de sapos: {0:.2f} %".format((statistic["S"] / total) * 100))