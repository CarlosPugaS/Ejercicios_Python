"""
Palabras que aparecen más de una vez
Pide una frase e imprime solo las palabras que se repiten, junto con su cantidad.
"""

phrase = input("Please insert a phrase : \n")
phrase = phrase.split()

count = {}

for word in phrase:
    word = word.lower()
    count[word] = count.get(word, 0) + 1
print("repeated words:")
for word, amount in count.items():
    if amount >= 2:
        print(f'{word} : {amount}')
