"""
Palabras exclusivas
Muestra las palabras que están en una frase pero no en la otra.
(Solo en la primera o solo en la segunda)

"""

phrase_one = input("Please insert a first phrase : \n")
phrase_two = input("Please insert a second phrase : \n")

set1 = set(word.lower() for word in phrase_one.split())
set2 = set(word.lower() for word in phrase_two.split())

unique1 = set1 - set2
unique2 = set2 - set1 

print(f'The exclusive words in the first phrase are : {unique1}')
print(f'The exclusive words in the second phrase are : {unique2}')