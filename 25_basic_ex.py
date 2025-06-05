"""
Contar cuántas veces aparece cada palabra en la frase
Pide una frase y muestra:
"""

frase = input("Ingrese una frase : \n")
lista_frase = frase.split()
contador = {}

for palabra in lista_frase:
    palabra = palabra.lower()
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1

for palabra, cantidad in contador.items():
    print(f'La palabra {palabra} esta {cantidad} veces en la frase.')
