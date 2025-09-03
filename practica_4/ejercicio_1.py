# A
def par_o_impar(n):
    "indica si el numero es par o impar"
    if n % 2 == 0:
        print(f"{n} es par")
    else:
        print(f"{n} es impar")


par_o_impar(5)


# B
def indicar_si_es_primo(n):
    "Indica si el numero es primo"
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(indicar_si_es_primo(12))