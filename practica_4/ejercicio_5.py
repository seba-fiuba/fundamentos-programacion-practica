def convertir_mes(mes):
    meses = {
        1: "enero",
        2: "febrero",
        3: "marzo",
        4: "abril",
        5: "mayo",
        6: "junio",
        7: "julio",
        8: "agosto",
        9: "septiembre",
        10: "octubre",
        11: "noviembre",
        12: "diciembre",
    }
    if 1 <= mes <= 12:
        return meses[mes]
    else:
        return None


def es_bisiesto(año):
    "Indica si el año ingresado es bisiesto o no"
    if año <= 0:
        return False
    bisiesto = (año % 4 == 0) and ((año % 100 != 0) or (año % 400 == 0))
    return bisiesto


año = es_bisiesto(2021)
if año:
    print("Es bisiesto")
else:
    print("No es bisiesto")

# b


def dar_dias_del_mes(mes, año):
    "Devuelve la cantidad de dias que tiene el mes"
    if not isinstance(mes, int):
        return False
    else:
        mes = mes.lower()
        meses_con_31 = [
            "enero",
            "marzo",
            "mayo",
            "julio",
            "agosto",
            "octubre",
            "diciembre",
        ]
        meses_30 = {"abril", "junio", "septiembre", "noviembre"}
        if mes == "febrero" and es_bisiesto(año):
            return 29
        elif mes == "febrero" and not es_bisiesto(año):
            return 28
        elif mes in meses_con_31:
            return 31
        elif mes in meses_30:
            return 30
        return None


dias = dar_dias_del_mes("febrero", 2024)
if dias is None:
    print("Mes invalido")
else:
    print(dias)


# c
def validar_fecha(dia, mes, año):
    "Valida si la fecha ingresada es valida"
    mes = convertir_mes(mes)
    if mes is None:
        return False
    if año <= 0 or not (1 <= dia <= 31):
        return False
    elif (
        not es_bisiesto(año)
        and mes == "febrero"
        and dia == 29
        or mes == "febrero"
        and dia > 29
    ):
        return False
    elif dar_dias_del_mes(mes, año) == 30 and dia > 30:
        return False

    return True


fecha = validar_fecha(12, 2, 2020)
if fecha:
    print("Fecha valida")
else:
    print("Fecha invalida")


# d
# Casos de prueba para validar_fecha
assert validar_fecha(29, 2, 2020) == True  # año bisiesto, debe ser válido
assert validar_fecha(29, 2, 2021) == False  # no bisiesto, 29 feb inválido
assert validar_fecha(31, 4, 2023) == False  # abril solo tiene 30
assert validar_fecha(30, 4, 2023) == True  # válido
assert validar_fecha(12, 13, 2023) == False  # mes 13 inválido

# Casos de prueba para dar_dias_del_mes
assert dar_dias_del_mes("octubre", 2023) == 31
assert dar_dias_del_mes(10, 2023) == 31
assert dar_dias_del_mes("pizza", 2023) is None
