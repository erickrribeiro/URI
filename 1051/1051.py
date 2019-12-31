x = float(input())
if x >= 0.00 and x <= 2000.00:
    print("Isento")
elif x > 2000.00 and x <= 3000.00:
    x = x - 2000.00
    imposto = x * 0.08
    print("R$ {0:.2f}".format(imposto))
elif x > 3000.00 and x <= 4500.00:
    imposto = 1000 * 0.08
    x = x - 3000.00
    imposto += x * 0.18
    print("R$ {0:.2f}".format(imposto))
elif x > 4500.00:
    imposto = 1000.00 * 0.08
    imposto += 1500.00 * 0.18
    x = x - 4500.00
    imposto += x * 0.28
    print("R$ {0:.2f}".format(imposto))




