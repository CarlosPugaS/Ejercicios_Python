"""
Detectar palabras comunes
Pide dos frases e imprime solo las palabras que ambas tienen en común (sin repetirlas).
"""

phrase_one = input("Please insert the first phrase: \n")
phrase_two = input("Please insert the second phrase: \n")

set1 = set(word.lower() for word in phrase_one.split())
set2 = set(word.lower() for word in phrase_two.split())

common = set1 & set2

print(f'The comun words are : {list(common)}')