"""
Números pares :
Pide 10 números y guarda solo los pares en una lista.
Al final, imprime la lista de pares y cuántos fueron.
"""

pares = []
contador = 0

while contador < 10:
    numero = int(input("Ingrese un digito : \n"))
    if numero % 2 == 0:
        pares.append(numero)
    contador += 1

print(f'los numeros pares fueron {pares} y fueron {len(pares)}')