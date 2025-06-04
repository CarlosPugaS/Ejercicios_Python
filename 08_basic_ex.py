"""
Pide un número positivo al usuario e imprime desde
ese número hasta 1, descendiendo uno por uno.
"""

numero = int(input("Ingrese un numero positivo"))
while numero > 0:
    print(numero)
    numero -= 1