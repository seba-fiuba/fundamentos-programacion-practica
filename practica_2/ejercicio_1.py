import math


def capital_final(pesos, interes, años):
    calculo_interes = pesos * (1 + (interes / 100)) ** años
    return calculo_interes
