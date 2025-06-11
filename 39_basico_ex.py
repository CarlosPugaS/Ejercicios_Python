"""
Detectar palabras comunes
Pide dos frases e imprime solo las palabras que ambas tienen en común (sin repetirlas).
"""

phrase_one = input("Please insert the first phrase: \n")
phrase_two = input("Please insert the second phrase: \n")

phrase_one = set(word.lower() for word in phrase_one.split())
print(phrase_one)
""" phrase_two = set(word.lower() for word in phrase_two.split())
print(phrase_two) """