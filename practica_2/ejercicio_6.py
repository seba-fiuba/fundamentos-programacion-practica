def numeros_pares():
    "Dado dos numeros imprime todos los numeros pares entre estos"
    inicio = int(input("Ingrese un numero: "))
    fin = int(input("Ingrese otro numero: "))

    for n in range(inicio, fin):
        if n % 2 == 0:
            print(n)


numeros_pares()
