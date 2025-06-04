""" 
Contador de palabras
- Crea un programa que:
- Pida al usuario una frase (una línea de texto).
- Cuente cuántas palabras contiene.
- Imprima: 'Total de palabras : X'
"""

frase = str(input("Escriba una frase para saber cuantas palabras tiene: \n"))
palabras = frase.split()
contador = len(palabras)

print(f'Total de palabras: {contador}')