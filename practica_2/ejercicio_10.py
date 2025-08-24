def fichas_juego(fin):
    "Imprime todas las fichas de domino"
    for n in range(0, fin):
        for i in range(n, fin):
            print(f"{n} | {i}")


fichas_juego(23)
