"""
Contar vocales
Pide una frase.
Cuenta cuántas veces aparece cada vocal (a, e, i, o, u)
Ignora mayúsculas y otras letras.
"""

phrase = input("Please insert a phrase:\n").lower()

vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

for letter in phrase:
    if letter in vowels:
        vowels[letter] += 1

for vocal, amount in vowels.items():
    print(f'{vocal}: {amount}')