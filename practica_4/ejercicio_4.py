def calcular_max_min_polinomio(a, b, c):
    "Dado a, b, c calcula max o minimo de un polinomio de segundo grado"
    
    x_vertice = -b/(2*a)
    y_vertice = ((4*a*c) - b**2) / (4*a)
    
    if a > 0:
        print(f"El minimo es: ({x_vertice}, {y_vertice})")
    else:
        print(f"El maximo es: ({x_vertice}, {y_vertice})")
        

calcular_max_min_polinomio(-3, 6, -2)

#B
def 