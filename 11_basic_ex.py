"""
Genera un número aleatorio entre 1 y 10.
El usuario debe adivinarlo.
Repite hasta que acierte
"""
import random

aleatorio_num = random.randint(1, 10)
user_num = 0

while aleatorio_num != user_num:
    user_num = int(input("Adivine el número aleatorio entre 1 y 10: "))

print(f"¡Correcto! El número era {aleatorio_num}")
