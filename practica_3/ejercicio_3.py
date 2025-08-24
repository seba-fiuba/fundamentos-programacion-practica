def mayor_producto(num1, num2, num3, num4):
    numeros = [num1, num2, num3, num4]
    producto = []

    for i in range(len(numeros)):
        for j in range(i + 1, len(numeros)):
            producto.append(numeros[i] * numeros[j])
    print(max(producto))


mayor_producto(2, 4, 6, 8)
