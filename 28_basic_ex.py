"""
Filtrar palabras únicas : 
- Pide una frase.
- Guarda en una nueva lista solo las palabras que aparecen una sola vez.
- Imprime esa lista.
"""

phrase = input("Escriba una frase : \n")
phrase = phrase.split()
save_words = []
unique_list = []

count = {}

for word in phrase:
    word = word.lower()
    if word.isalpha():
        count[word] = count.get(word, 0) + 1
    
for word, amount in count.items():
    if amount == 1:
        unique_list.append(word)
        print(unique_list)