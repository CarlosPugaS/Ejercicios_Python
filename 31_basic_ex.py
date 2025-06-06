"""
Solicita una frase al usuario.
- Invierte cada palabra, pero mantén el orden de las palabras.
- Imprime la frase resultante.
ejemplo : 
Entrada:  Hola mundo
Salida:   aloH odnum
"""

frase = input("Ingresa una frase : \n")
frase = frase.split()
frase_invertida = []

for palabra in frase:
    palabra_invertida = palabra[::-1]
    frase_invertida.append(palabra_invertida)

print(f'entrada : {frase} \nsalida : {frase_invertida}')