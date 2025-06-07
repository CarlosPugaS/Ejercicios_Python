"""
Palabras con la misma longitud
- Pide una frase.
- Agrupa las palabras por longitud, y muestra algo como:
Palabras de 2 letras: ['de', 'la']
Palabras de 5 letras: ['luz', 'casa']
Palabras de 6 letras: ['verde']
"""

phrase = input("Please, insert a phrase : \n")
phrase = phrase.split()
group = {}

for word in phrase: 
    word = word.lower()
    large = len(word)
    if large not in group:
        group[large] = [word]
    else:
        group[large].append(word)
for large, word in group.items():
    print(f'Palabras de {large} letras: {word} \n')
