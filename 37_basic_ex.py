"""
Frase palíndromo?
Pide una frase.
Ignora mayúsculas y espacios.
Determina si la frase es un palíndromo completo (se lee igual al revés).
"anita lava la tina" → Es_palindromo
"hola mundo" → No_es_palindromo
"""

phrase = input("Please insert a phrase : \n")
phrase = phrase.split()

phrase = "".join(phrase).lower()
print(phrase)

if phrase == phrase[::-1]:
    print("The phrase is a palindrome")
else:
    print("The phrase is not a palindrome")
