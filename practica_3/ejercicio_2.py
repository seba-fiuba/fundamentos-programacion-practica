from ejercicio_1 import convertir_a_segundos, convertir_a_horas


def main():
    "Recibe 2 lapsos de horas, minutos y segundos y devuelve la suma de ambos"
    hora1 = int(input("Ingrese la hora: "))
    minutos1 = int(input("Ingrese los minutos: "))
    segundos1 = int(input("Ingrese los segundos: "))
    hora2 = int(input("Ingrese la hora: "))
    minutos2 = int(input("Ingrese los minutos: "))
    segundos2 = int(input("Ingrese los segundos: "))
    hora_total = hora1 + hora2
    minutos_total = minutos1 + minutos2
    segundos_total = segundos1 + segundos2
    segundos = convertir_a_segundos(hora_total, minutos_total, segundos_total)
    fin = convertir_a_horas(segundos)
    print(fin)


main()
