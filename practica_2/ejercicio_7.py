def numeros_triangulares():
    "Se le pide un numero al usuarioe imprime los prmeros n numeros triangulares junto a su indice"
    n = int(input("Ingrese un numero: "))
    suma = 0
    for i in range(1, n + 1):
        suma += i
        print(f"{i} - {suma}")


numeros_triangulares()
