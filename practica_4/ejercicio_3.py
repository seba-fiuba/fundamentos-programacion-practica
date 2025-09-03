def matriz_identidad(dimension):
    "devuelve una matriz identidad de la dimension indicada"
    matriz = []
    for fila_idx in range(dimension):
        fila = []
        for col_idx in range(dimension):
            if fila_idx == col_idx:
                fila.append(1)
            else:
                fila.append(0)
        matriz.append(fila)
    return matriz

m = matriz_identidad(3)
for fila in m:
    print(fila)   
              