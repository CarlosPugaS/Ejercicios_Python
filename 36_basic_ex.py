"""
Invertir orden de palabras (no letras)
Pide una frase.
Invierte el orden de las palabras, pero no las letras.

Ejemplo:
        Entrada:  hola mundo esto es python
        Salida:   python es esto mundo hola
"""

phrase = input("Please, insert a phrase : \n")
phrase = phrase.split()
print(f'Input : {phrase}')
phrase.reverse()
print(f'Output : {phrase}')

