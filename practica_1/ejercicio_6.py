# A- dados 2 numeros imprimir la suma, resta, division y multiplicacion de ambos


def operacion_con_numeros(n1, n2):
    suma = n1 + n2
    resta = n1 - n2
    division = n1 / n2
    multiplicacion = n1 * n2
    print(
        f" suma: {suma} | resta: {resta} | division: {division} | multiplicacion: {multiplicacion}"
    )


operacion_con_numeros(34, 6)


# B- Dado un natural imprimir su tabla de multiplicar


def tabla_multiplicar(natural):
    for n in range(1, 11):
        multiplo = n * natural
        print(f"{natural} X {n} = {multiplo}")


tabla_multiplicar(4)
