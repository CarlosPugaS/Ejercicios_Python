"""
Diccionario de contacto
Crea un programa que:
- Pida nombre, teléfono y email.
- Los guarde en un diccionario.
- Luego imprima el contenido así:
"""

nombre = input("Ingrese su nombre : \n")
telefono = input("Ingrese su numero de telefono: \n")
correo = input("Ingrese su correo electronico: \n")


diccionario = {
    "Nombre": nombre,
    "Telefono": telefono,
    "Correo": correo
}

print('\nSus datos son : ')
print(f'Nombre : {diccionario['Nombre']}')
print(f'Telefono : {diccionario["Telefono"]}')
print(f'Correo : {diccionario["Correo"]}')