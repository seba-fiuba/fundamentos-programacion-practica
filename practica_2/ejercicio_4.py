from ejercicio_3 import convertir_a_celsius


def main():
    for n in range(0, 121, 10):
        grado = convertir_a_celsius(n)
        print(f"{n}F = {grado}C")


main()
