again = 1
total = 0
inter_wins = 0
gremio_wins = 0 
draw = 0

while again == 1:
    I, G = input("").split()
    I = int(I)
    G = int(G)

    if I == G:
        draw += 1
    if I > G:
        inter_wins += 1
    else: 
        gremio_wins += 1

    again = int(input("Novo grenal (1-sim 2-nao)\n"))
    total += 1

print("{} grenais".format(total))
print("Inter:{}".format(inter_wins))
print("Gremio:{}".format(gremio_wins))
print("Empates:{}".format(draw))

if inter_wins > gremio_wins:
    print("Inter venceu mais")
elif inter_wins > gremio_wins:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")



     