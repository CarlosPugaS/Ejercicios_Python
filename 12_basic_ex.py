""" 
Genera un número aleatorio entre 1 y 10.
El usuario debe adivinarlo.
El usuario solo tendra 3 intentos para poder adivinar el numero
"""
import random

print("Adivine el número secreto. Tiene solo 3 intentos.\n")

random_num = random.randint(1, 10)
intentos = 0
user_num = 0

while user_num != random_num and intentos < 3:
    user_num = int(input(f'Intento numero {intentos + 1} : \n'))
    intentos += 1

    if random_num != user_num:
        print("Incorrecto intente nuevamente !")
    else:
        print("Has adivinado, felicitaciones !")

if user_num != random_num:
    print(f'Has perdido, el numero secreto era {random_num}.')