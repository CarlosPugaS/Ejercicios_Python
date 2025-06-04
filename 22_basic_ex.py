# Lee el archivo Agenda.txt creado en el ejercicio 
# anterior e imprime cada contacto.

with open("Agenda.txt", "r") as archivo:
    lineas = archivo.readlines()

for linea in lineas:
    datos = linea.strip().split(",")
    nombre = datos[0].strip()
    telefono = datos[1].strip()
    correo = datos[2].strip()

print(f"Nombre: {nombre}")
print(f"Teléfono: {telefono}")
print(f"Correo: {correo}\n")