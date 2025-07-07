# Desafío: ¡Contar Elementos Únicos y Frecuencias!

# Escribe una función que tome una lista de elementos (que pueden ser números o cadenas de texto) 
# y devuelva un diccionario donde las claves sean los elementos únicos de la lista y los valores sean 
# el número de veces que cada elemento aparece en la lista.
from collections import Counter


def unicos_y_frecuentes():
    lista_frutas = ["manzana", "banana", "manzana", "pera", "banana", "manzana"]
    # dic_contador = {}

    # for fruta in lista_frutas:
    #     if fruta in dic_contador:
    #         dic_contador[fruta] += 1
    #     else:
    #         dic_contador[fruta] = 1
    # print(dic_contador)
    # return dic_contador

    # for fruta in lista_frutas:
    #     dic_contador[fruta] = dic_contador.get(fruta, 0) + 1
    # print(dic_contador)
# Forma mas concisa utilizando el modulo collections > Counter 
    dict_contador = Counter(lista_frutas)
    print(dict_contador)


unicos_y_frecuentes()
