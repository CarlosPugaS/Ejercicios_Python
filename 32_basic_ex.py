"""
Palabras palíndromo
Pide una frase e imprime solo las palabras que son palíndromos (se leen igual al revés).
Ejemplo: "oso", "reconocer", "anilina"
"""

phrase = input("Please insert a phrase : \n")
phrase = phrase.split()
palindrome = []

for word in phrase:
    word = word.lower()
    if word == word[::-1]:
        palindrome.append(word)

print(f'The words that are palindromes are: : {" ".join(palindrome)}')
