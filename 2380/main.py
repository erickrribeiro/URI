class Banco:
    def __init__(self, id):
        self.id = id
        self.dono = self
        self.rank = 0

def buscaDono(banco):
    if banco.dono is not banco:
        banco.dono = buscaDono(banco.dono)
    return banco.dono

def uniao(x,y):
    xdono = buscaDono(x)
    ydono = buscaDono(y)

    if xdono is ydono:
        return

    if xdono.rank < ydono.rank:
        xdono, ydono = ydono, xdono

    ydono.dono = xdono
    if xdono.rank == ydono.rank:
        xdono.rank = xdono.rank + 1

if __name__ == '__main__':
    [n, b] = input().split()
    n = int(n)
    b = int(b)

    bancos = dict()
    for i in range(1, n + 1):
        bancos[i] = Banco(str(i))

    for i in range(1, b + 1):
        op = input()
        [type_op, b1, b2] = op.split()
        b1 = int(b1)
        b2 = int(b2)

        if type_op == 'F':
            uniao(bancos[b1], bancos[b2])
        elif type_op == 'C':
            if buscaDono(bancos[b1]).id == buscaDono(bancos[b2]).id:
                print("S")
            else:
                print("N")
