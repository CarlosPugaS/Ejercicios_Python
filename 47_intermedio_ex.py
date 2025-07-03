# Problema: Escribe una función que cuente el número de vocales en una cadena de texto dada. 
# Las vocales son 'a', 'e', 'i', 'o', 'u' (tanto en mayúsculas como en minúsculas).

def contar_vocales():

    cadena = input("ingresa una palabra: \n")
    vocales = "aeiou"
    contador_vocales = sum(1 for caracter in cadena.lower() if caracter in vocales)
    print(contador_vocales)


contar_vocales()