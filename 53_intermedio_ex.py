# Desafío: Encontrar el Elemento Más Frecuente

#Problema: Escribe una función que tome una lista de elementos (que pueden ser números o cadenas de texto)
#y devuelva el elemento que aparece más veces en la lista. Si hay un empate 
#(varios elementos tienen la misma frecuencia máxima), tu función puede devolver cualquiera de ellos.
from collections import Counter

""" def mas_apariciones():
    lista = ["manzana", "banana", "manzana", "pera", "banana", "manzana"]
    contador = {}
    mas_veces = ""
    cuantas = 0
    for elemento in lista:
        contador[elemento] = contador.get(elemento, 0) + 1

    for i, cantidad in contador.items():
        if cantidad > cuantas:
            cuantas = cantidad
            mas_veces = i
    print(f'{mas_veces} {cuantas}')


mas_apariciones() """


def mas_apariciones():
    """ Utilizando max() para obtener solo el nombre del item que tiene el mayor valor"""
    lista = ["manzana", "banana", "manzana", "pera", "banana", "manzana"]
    contador = Counter(lista)
    mas_veces = max(contador.keys(), key=contador.get)
    print(mas_veces)
# Solo retornamos la clave, la comparacion la realizamos accediendo al valor de la llave con contador.get


mas_apariciones()


def mas_apariciones_con_cantidad():
    """ Obteniendo clave-valor con max() """

    lista = ["manzana", "banana", "manzana", "pera", "banana", "manzana"]
    contador = Counter(lista)
    mas_frecuente, cantidad = max(contador.items(), key=lambda item: item[1])
    print(f"El elemento con más apariciones es: '{mas_frecuente}' ({cantidad} veces)")
# lambda item: item[1] - Funcion anonima toma una tupla (item) y 
# usa a max para buscar el segundo elemento de la tupla Que en este caso es 
# cantidad para realizar la comparacion.


mas_apariciones_con_cantidad()