from practica_1.ejercicio_5 import calcular_factorial


def main():
    "El usuario ingresa un número y se imprime por pantalla el factorial de ese número"
    print("Bienvenido a la calculadora de factorial!")
    usuario = input("Ingrese un número o X para salir: ").upper()
    while usuario != "X":
        try:

            usuario = int(usuario)
            factorial = calcular_factorial(usuario)
            print(f"{usuario}! = {factorial}")
            usuario = input("Ingrese otro número o X para salir: ").upper()
        except ValueError:
            print("No ha ingresado una opción valida")
            usuario = input("Por favor ingrese un número o X para salir: ").upper()

    print("Adios!")


def opcion_2():
    usuario = int(input("Ingrese un numero: "))
    for n in range(1, usuario + 1):
        print(f"{n}! = {calcular_factorial(n)}")


opcion_2()
