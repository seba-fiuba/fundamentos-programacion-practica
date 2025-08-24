# A
def impar_o_par(n):
    "Si el numero es par devuelve un 1 y si es impar un 0"
    if n % 2 == 0:
        return 1
    else:
        return 0


print(impar_o_par(143))


# B
def cantidad_unidades(n):
    "Recibe un numero y devuelve la cantidad de digitos"
    numero = str(n)
    print(len(numero))


cantidad_unidades(123)


# C
def multiplo_de_10(n):
    "Recibe un numero y devuelve el primer multiplo de 10 inferior a el"
    while n % 10 != 0:
        n -= 1
    print(n)


multiplo_de_10(123)
