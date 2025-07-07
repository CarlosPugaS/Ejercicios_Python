# Desafío: Suma de Elementos Pares
# Problema: Escribe una función que tome una lista de números enteros como
# entrada y devuelva la suma de solo los números pares de esa lista.

""" def sumar_pares():
    lista_numeros = [1, 2, 3, 4, 5, 6, 0, -1, -4]
    suma = 0
    for numeros in lista_numeros:
        if numeros % 2 == 0:
            suma = suma + numeros
    return suma

sumar_pares() """


def sumar_pares():
    """ Forma mas eficiente de llegar al resultado"""

    lista_numeros = [1, 2, 3, 4, 5, 6, 0, -1, -4]
    contador_pares = sum(numeros for numeros in lista_numeros if numeros % 2 == 0)
    print(contador_pares)


sumar_pares()
