"""
Escribe un programa que:
- Pida por consola los siguientes datos:
- Tu edad
- Tu estatura
- Tu nombre completo
- Si estás estudiando programación (sí o no)
Asigne esos datos a las variables respectivas.
Muestra todas las variables juntas en una sola línea de texto
"""

edad = int(input("Ingrese su edad"))
estatura = float(input("Ingrese su estatura"))
nombre = input("Ingrese su nombre completo")
es_estudiante = input("Es usted estudiante? (si / no)").lower
if es_estudiante == "si":
    es_estudiante = "si"
else:
    es_estudiante = "no"

print(f'Su nombre es {nombre} tiene {edad} mide {estatura} y {es_estudiante} estudia')