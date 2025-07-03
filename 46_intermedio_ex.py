# Invertir una cadena de texto : 
# Problema: Escribe una función que tome una cadena de texto como entrada y devuelva esa cadena invertida.
# "Hola" debería devolver "aloH"

def invertir_cadena():
    cadena = input("Ingrese una palabra : \n")
    cadena_invertida = cadena[::-1]
    print(cadena_invertida)


invertir_cadena()