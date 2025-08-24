import math


# A- perimetro de un rectangulo
def calcular_perimetro_rectangulo(base, altura):
    perimetro = 2 * (base + altura)
    return perimetro


# B- Area de un rectangulo
def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area


# C- Area de rectangulo alineado con los ejes x e y dadas sus coordenadas x1, x2, y1, y2


def calcular_area_rectangulo_2(x1, x2, y1, y2):
    base = x2 - x1
    altura = y2 - y1
    area = base * altura
    return area


# D- perimetro de un circulo dado su radio


def perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro


# E-area de un circulo
def area_circulo(radio):
    area = math.pi * (radio**2)
    return area


# F- volumen de una esfera


def volumen_esfera(radio):
    volumen = (4 / 3) * math.pi * radio**3
    return volumen


# G- Hipotenusa
def calcular_hipotenusa(opuesto, adyacente):
    hipotenusa = math.sqrt(opuesto**2 + adyacente**2)
    return hipotenusa
