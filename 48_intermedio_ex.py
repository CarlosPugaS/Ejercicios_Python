# Desafío Diario: Encontrar el Número Máximo
# Problema: Escribe una función que tome una lista de números enteros como entrada y devuelva el número entero más grande de esa lista.
# Consideraciones:
# La lista podría contener números positivos, negativos o cero.
# Asume que la lista de entrada no estará vacía.

# Ejemplos:

# [1, 5, 2, 8, 3] debería devolver 8
# [10, -2, 30, 5] debería devolver 30
# [-1, -5, -2] debería devolver -1
# [7] debería devolver 7


def numero_mayor():
    
    listaDeNumeros = [15, 87, 32, 5, 91, 44, 76]
    mas_grande = max(listaDeNumeros)
    print(mas_grande)


numero_mayor()