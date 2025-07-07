# Desafío Diario: Palíndromos
# Escribe una función que determine si una cadena de texto dada es un palíndromo. 
# Un palíndromo es una palabra o frase que se lee igual de adelante hacia atrás 
# que de atrás hacia adelante, ignorando espacios y mayúsculas/minúsculas.

def es_Palindromo():
    palabra = input("Ingresa una palabra: \n").lower().strip()
    if palabra == palabra[::-1]:
        print("La palabra es un palindromo! ")
    else:
        print("La palabra no es un palindromo")

es_Palindromo()