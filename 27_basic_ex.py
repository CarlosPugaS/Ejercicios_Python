"""
contar_letras_frase(frase)
Convierte tu función en una que reciba una frase como parámetro, y cuente letras en toda la frase.
"""


def contar_letras_frase(frase):
    contador = {}

    for letra in frase:
        letra = letra.lower()
        if letra.isalpha():  # Solo si la letra es alphanumerica
            contador[letra] = contador.get(letra, 0) + 1 
            # Busco la clave letra en el dict contado -> Si existe retorna su valor +1, si no retorna 0+1 x defecto
    for letra, cantidad in contador.items():
        print(f'La letra "{letra}" aparece {cantidad} de veces.')


contar_letras_frase("paralelepipedo")