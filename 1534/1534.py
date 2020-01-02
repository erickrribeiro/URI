while True:
    try:
        n = int(input())
        if n < 3:
            continue
        if n > 69:
            continue
        for i in range(n):
            for j in range(n):
                if i + j == n -1:
                    print(2, end="")
                elif i == j:
                    print(1, end="")
                else:
                    print(3, end="")
            print()
    except EOFError:
        print()
        break
    