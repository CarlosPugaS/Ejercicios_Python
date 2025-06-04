"""
Pide una frase y muestra cuál es la palabra más larga que contiene.
"""

frase = input("Escribe una frase y te dire la palabra mas larga \n")

lista_frase = frase.split()
max_larga = 0
palabra_larga = ""

for palabra in lista_frase:
    if len(palabra) > max_larga:
        max_larga = len(palabra)
        palabra_larga = palabra

print(f'La palabra mas larga es : {palabra_larga} con {max_larga} caracteres.')