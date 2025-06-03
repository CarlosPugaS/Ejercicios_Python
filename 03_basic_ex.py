""" Ahora trabajaremos con números. Escribe un programa que:
Pida dos números enteros al usuario.
Calcule y muestre:
La suma
La resta
La multiplicación
La división
El resto (módulo) """

num_uno = int(input("Ingrese un numero entero"))
operacion = input("Que operacion desea realizar? indique (+ - * / %) ")
num_dos = int(input("Ingrese otro numero entero"))

if operacion == "+":
    resultado = num_uno + num_dos
    print(f'La suma de {num_uno} + {num_dos} es {resultado}')

elif operacion == "-": 
    resultado = num_uno - num_dos
    print(f'La resta de {num_uno} - {num_dos} es {resultado}')

elif operacion == "*":
    resultado = num_uno * num_dos
    print(f'La multiplicacion de {num_uno} * {num_dos} es {resultado}')

elif operacion == "/":
    resultado = num_uno / num_dos
    print(f'La division de {num_uno} / {num_dos} es {resultado}')
elif operacion == "%":
    resultado = num_uno % num_dos
    print(f'El resto de {num_uno} % {num_dos} es {resultado}')
else:
    print("Operación no valida! ")
