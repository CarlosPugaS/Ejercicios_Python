"""
Palabra más frecuente
Pide una frase.
Encuentra cuál es la palabra que más veces se repite.
Imprime esa palabra y cuántas veces aparece.
"""

phrase = input("Please inser a phrase : \n")
phrase = phrase.split()
count = {}

for word in phrase: 
    word = word.lower()
    count[word] = count.get(word, 0) + 1

more_times = 0
more_frequent = ""
for word, amount in count.items():
    if amount > more_times:
        more_times = amount
        more_frequent = word
print(f'the phrase that is repeated most is : {more_frequent} with {more_times} times.')
