"""
Contar consonantes
Pide una frase.
Cuenta cuántas veces aparece cada consonante
(sin vocales, sin signos, sin espacios).
"""

phrase = input("Please insert a phrase : \n").lower()

consonants = {"b": 0, "c": 0, "d": 0, "f": 0, "g": 0, "h": 0,
              "j": 0, "l": 0, "k": 0, "m": 0, "n": 0, "ñ": 0,
              "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "v": 0,
              "x": 0, "w": 0, "y": 0, "z": 0}

for letter in phrase:
    if letter in consonants:
        consonants[letter] += 1

for consonante, amount in consonants.items():
    print(f'{consonante} = {amount}')
