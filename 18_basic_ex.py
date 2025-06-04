"""
suma_pares_impares(lista)
Crea una función que reciba una lista y retorne dos valores:
La suma de los pares
La suma de los impares
"""


def sumar_pares_impares(lista):
    sumar_pares = 0
    sumar_impares = 0
    for i in lista:
        if i % 2 == 0:
            sumar_pares += i
        else:
            sumar_impares += i
    return sumar_pares, sumar_impares


lista = list(range(1, 20))

resultado = sumar_pares_impares(lista)
print(f'La suma de los pares fue {resultado[0]} y los impares {resultado[1]}')