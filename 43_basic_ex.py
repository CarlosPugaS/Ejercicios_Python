"""
Mejora del ejercicio 42 con modulo string 
"""

import string

phrase = input("Please insert a phrase: \n").lower()
vowels = {"a", "e", "i", "o", "u"}
consonants = {letter: 0 for letter in string.ascii_lowercase if letter not in vowels}

for letter in phrase:
    if letter in consonants:
        consonants[letter] += 1

for c, a in consonants.items():
    if a > 0:
        print(f'{c} = {a}')