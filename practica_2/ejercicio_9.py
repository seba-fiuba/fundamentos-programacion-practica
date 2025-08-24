def fichas_domino():
    "Imprime todas las fichas de domino"
    for n in range(0, 7):
        for i in range(n, 7):
            print(f"{n} | {i}")


fichas_domino()
