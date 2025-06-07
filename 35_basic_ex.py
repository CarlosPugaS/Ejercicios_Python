"""
Palabras únicas y repetidas por separado
-Pide una frase.
-Imprime dos listas:
    Palabras que aparecen solo una vez
    Palabras que aparecen más de una vez
"""

phrase = input("Please insert a phrase : \n")
phrase = phrase.split()
all_words = {}
once = []
repeat = []

for word in phrase:
    word = word.lower()
    all_words[word] = all_words.get(word, 0) + 1

for word, amount in all_words.items():
    if amount >= 2:
        repeat.append(word)
    else:
        once.append(word)

print(f'The words that are only there once : {once}')
print(f'The words that are repeated : {repeat}')
