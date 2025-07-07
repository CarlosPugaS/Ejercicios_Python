# Desafío Diario: Contar Palabras en una Frase

# Problema: Escribe una función que tome una cadena de texto (una frase) 
# como entrada y devuelva el número total de palabras en esa frase.

def contar_palabras():
    frase = input("Escriba una frase: \n").strip()
    frase = frase.split()
    print(len(frase))

contar_palabras()