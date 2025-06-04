"""
Ejercicio 13: Promedio de notas
Pide al usuario que ingrese 5 notas (0 a 10).
Guárdalas en una lista.
Muestra el promedio.
"""

print("Ingrese 5 notas de 0 a 10")
nota_uno = int(input("Ingrese la primer nota\n"))
nota_dos = int(input("Ingrese la segunda nota\n"))
nota_tres = int(input("Ingrese la tercera nota\n"))
nota_cuatro = int(input("Ingrese la cuarta nota\n"))
nota_cinco = int(input("Ingrese la quinta nota\n"))

notas = [nota_uno, nota_dos, nota_tres, nota_cuatro, nota_cinco]
suma = 0
for nota in notas:
    suma = nota + suma
print(f'El promedio de notas es {suma/5}')