"""
Escribe un programa que:
- Pida un número entero positivo.
- Mientras el número no sea positivo, vuelva a pedirlo.
- Cuando el número sea válido, imprime: "Número válido: X".
"""

numero = 0

while numero <= 0:
    numero = int(input("Ingrese un número entero positivo: "))

print(f"Número válido: {numero}")
