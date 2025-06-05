"""
Función contar_letras(palabra)
Crea una función que cuente cuántas veces aparece cada letra en una palabra.
Ejemplo de salida:
"l": 2  
"o": 1 
"""


def contar_letras():

    palabra = input("Ingrese una palabra para contar cuantas veces se repiten las letras en ella : \n")
    contador = {}

    for letras in palabra:
        letras = letras.lower()
        if letras in contador:
            contador[letras] += 1
        else:
            contador[letras] = 1
    for letras, cantidad in contador.items():
        print(f'La letra {letras} esta {cantidad} veces en la palabra')  


contar_letras()