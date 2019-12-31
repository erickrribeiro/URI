n = int(input(""))
t = 0
for i in range(n):
    PA, PB, G1, G2 = input("").split()
    PA = int(PA)
    PB = int(PB)
    G1 = float(G1)
    G2 = float(G2)

    while(PA <= PB and t < 101):
        t += 1
        PA += int(PA * (G1 /100.00))
        PB += int(PB * (G2 /100.00))
        
    if t > 100:
        print("Mais de 1 seculo.")
    else:
        print("{} anos.".format(t))
    t = 0
        