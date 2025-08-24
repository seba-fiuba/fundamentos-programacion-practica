from ejercicio_1 import capital_final


def main():
    "Recibe capital inicial, tasa de interes y años y devuelve el capital final"
    pesos_inicial = int(input("Ingrese la cantidad de pesos iniciales: "))
    tasa_interes = int(input("Ingrese la tasa de interes: "))
    años = int(input("Ingrese el total de años: "))
    total = capital_final(pesos_inicial, tasa_interes, años)
    print(f"El capital total va ser de: {total}")


main()
