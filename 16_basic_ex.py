"""
Clasificar positivos y negativos
Pide 7 números al usuario.
Clasifícalos en dos listas: positivos y negativos.
Imprime ambas listas al final.
"""

positivos = []
negativos = []
contador = 0

while contador < 7:
    numero = int(input(f'Ingrese el numero {contador + 1} de 7: \n'))
    if numero > 0:
        positivos.append(numero)
    else:
        negativos.append(numero)
    contador += 1

print(f'Los numeros positivos fueron {positivos} y los negativos {negativos}')