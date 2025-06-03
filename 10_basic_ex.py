"""
Pide al usuario que ingrese 5 numeros enteros. Al final, muestra la suma total.
"""
contador = 0
suma_total = 0

while contador < 5:
    numero = int(input(f"ingrese el numero {contador+1}:\n"))
    suma_total += numero
    contador += 1
print(f"La suma total de sus numeros es {suma_total}")