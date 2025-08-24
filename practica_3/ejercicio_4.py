import math


# A
def calcular_norma_vector(x, y, z):
    "La función recibe 3 coordenadas de un vector y calcula la norma de este"
    norma = math.sqrt(x**2 + y**2 + z**2)
    return norma


print(calcular_norma_vector(12, 5, 2))


# B
def resta_vectores(x1, y1, z1, x2, y2, z2):
    "Realiza la resta entre 2 vectores de R3"
    vector_1 = [x1, y1, z1]
    vector_2 = [x2, y2, z2]
    vector_final = []
    for i in range(len(vector_1)):
        vector_final.append(vector_1[i] - vector_2[i])
    return vector_final


print(resta_vectores(2, 4, 6, 8, 2, 6))


# C
def calcular_producto_vectorial(x1, y1, z1, x2, y2, z2):
    "Recibe 2 vecores de R3 y devuelve el producto vectorial"
    vector_1 = [x1, y1, z1]
    vector_2 = [x2, y2, z2]
