"""
Guardar contactos en archivo
Toma la agenda creada y guarda cada contacto en un archivo .txt, uno por línea.
"""


lista = []

while True:
    nombre = input("Ingrese su nombre : \n")
    if nombre.lower() == "salir":
        break
    telefono = input("Ingrese su numero de telefono: \n")
    correo = input("Ingrese su correo electronico: \n")

    contacto = {
        "Nombre": nombre,
        "Telefono": telefono,
        "Correo": correo
    }
    lista.append(contacto)

print("\n La agenda sera guardada en el archivo Agenda.txt : ")
with open("Agenda.txt", "w") as archivo:
    for contacto in lista: 
        linea = f'{contacto["Nombre"]}, {contacto["Telefono"]}, {contacto["Correo"]}\n'
        archivo.write(linea)
