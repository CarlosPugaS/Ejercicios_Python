"""
Comparar frases
Pide dos frases al usuario.
Imprime si contienen las mismas palabras, sin importar el orden.
"""

phrase_one = input("Please inser a phrase for comparing : \n")
phrase_two = input("Please inser a phrase for comparing : \n")

phrase_one = phrase_one.split()
phrase_two = phrase_two.split()

set1 = set(phrase_one)
set2 = set(phrase_two)

if set1 == set2:
    print("The phrases is the same")
