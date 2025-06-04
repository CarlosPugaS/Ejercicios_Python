# Crea una función que reciba una lista de enteros y retorne la suma solo de los pares.

def sumar_pares(lista):
    suma = 0
    for i in lista: 
        if i % 2 == 0:
            suma += i
    return suma


lista = list(range(0, 10))
resultado = sumar_pares(lista)
print(f'La suma de los pares es: {resultado}')
