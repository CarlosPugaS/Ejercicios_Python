"""
Comparar frases
Pide dos frases al usuario.
Imprime si contienen las mismas palabras, sin importar el orden.
"""

phrase_one = input("Please inser a phrase for comparing : \n")
phrase_two = input("Please inser a phrase for comparing : \n")

set1 = set(word.lower() for word in phrase_one.split()) 
set2 = set(word.lower() for word in phrase_two.split())

if set1 == set2:
    print("The phrases contain the same words.")
else:
    print("The phrases do not contain the same words.")