# A
def convertir_a_segundos(horas, minutos, segundos):
    "Convierte a segundos un intervalo dado en horas minutos y segundos"
    total = 3600 * horas + 60 * minutos + segundos
    return total


convertir_a_segundos(12, 34, 43)


# B
def convertir_a_horas(s):
    "convierte segundos a horas, minutos y segundos"
    horas = s // 3600
    resto_hora = s % 3600
    minutos = resto_hora // 60
    segundos = resto_hora % 60
    return f"{horas}hs {minutos}min {segundos}s"


convertir_a_horas(45932)
