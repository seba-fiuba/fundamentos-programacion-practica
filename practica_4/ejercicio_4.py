import math
import cmath
from fractions import Fraction


# def calcular_max_min_polinomio(a, b, c):
#     "Dado a, b, c calcula max o minimo de un polinomio de segundo grado"

#     x_vertice = -b / (2 * a)
#     y_vertice = ((4 * a * c) - b**2) / (4 * a)

#     if a > 0:
#         print(f"El minimo es: ({x_vertice}, {y_vertice})")
#     else:
#         print(f"El maximo es: ({x_vertice}, {y_vertice})")


# calcular_max_min_polinomio(-3, 6, -2)


# B
def calcular_raices(a, b, c):
    "Calcula las raices de un polinomio de segundo grado"
    discriminante = b**2 - (4 * a * c)
    divisor = 2 * a
    if discriminante >= 0 and divisor != 0:
        raiz = math.sqrt(discriminante)
        x1 = ((-b) + raiz) / divisor
        x2 = ((-b) - raiz) / divisor
        print(f"las raices son: x1= {x1} y x2= {x2}")
    elif discriminante < 0 and divisor != 0:
        print(
            f"las raices son: x1= {-b} + i√{abs(discriminante)} / {divisor} y x2= {-b} - i√{abs(discriminante)} / {divisor}"
        )
    else:
        print("no se puede dividir por 0")


calcular_raices(1, 0, 2)


def calcular_raices_2(a, b, c):
    if a == 0:
        print("No se puede dividir por 0 y no es un pol de grado 2")
        return
    discriminante = b**2 - (4 * a * c)
    divisor = 2 * a
    raiz = cmath.sqrt(discriminante)
    x1 = (-b + raiz) / divisor
    x2 = (-b - raiz) / divisor
    print(f"Las raices son: x1= {x1} y x2= {x2}")


calcular_raices_2(1, 1, 2)


# C
def interseccion_rectas(m1, b1, m2, b2):
    "Calcula el (x,y) donde se cruzan las rectas"
    if m1 == m2 and b1 == b2:
        print("Son la misma recta")
        return
    elif m1 == m2:
        print("Son paralelas no se cortan")
        return
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    print(f"Las rectas se cruzan en el punto(x,y) = ({x}, {y})")


interseccion_rectas(2, 3, 5, -2)
