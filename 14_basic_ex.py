"""
Suma hasta que el usuario escriba 0 :
- Pide números al usuario uno por uno.
- Cuando escriba 0, termina.
- Muestra la lista de números y su suma total.
"""

suma = 0
lista_digitos = []

while True:
    numero = (int(input("Ingrese un digito para sumar, o Cero para salir : \n")))
    if numero == 0:
        break
    lista_digitos.append(numero)
    suma += numero

print(f'Numeros ingresados : {lista_digitos}')
print(f'Suma total de los digitos ingresados : {suma}')
