"""
Agenda :
- Permite al usuario guardar varios contactos (nombre, teléfono, email) en una lista de diccionarios.
- Finaliza cuando el usuario escriba "salir" como nombre.

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

print("\n Agenda : ")
for contacto in lista: 
    print(f'Nombre : {contacto['Nombre']}')
    print(f'Telefono : {contacto['Telefono']}')
    print(f'Correo : {contacto['Correo']}')