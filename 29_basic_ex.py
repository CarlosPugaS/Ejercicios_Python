"""
Palabras ordenadas por longitud
Objetivo:
- Pide al usuario una frase.
- Convierte esa frase en una lista de palabras.
- Ordena las palabras de mayor a menor según su longitud.
- Imprímelas, una por línea.
"""

phrase = input("Please insert a phrase : \n")

phrase = phrase.split()
phrase.sort(key=len, reverse=True)
for word in phrase:
    print(f'{word}\n')