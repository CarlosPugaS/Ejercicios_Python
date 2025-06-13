"""
Ejercicio 45: Validar contraseña segura
Verifica que una contraseña contenga:
al menos 8 caracteres
una mayúscula
una minúscula
un número
un símbolo (como !, @, #, etc.)
"""

password = input("Ingrese una contraseña : \n")

simbolos = "!@#$%^&*()_+-=[]{},.<>/?"
tiene_mayuscula = False
tiene_minuscula = False
tiene_numero = False
tiene_simbolo = False

for caracter in password:
    if caracter.isupper():
        tiene_mayuscula = True
    elif caracter.islower():
        tiene_minuscula = True
    elif caracter.isdigit():
        tiene_numero = True
    elif caracter in simbolos:
        tiene_simbolo = True

if len(password) < 8:
    print("La contraseña debe tener al menos 8 caracteres")        
if not tiene_mayuscula:
    tiene_mayuscula = False
    print("La contraseña debe tener al menos una letra mayúscula")
if not tiene_minuscula:
    tiene_minuscula = False
    print("La contraseña debe tener al menos una letra minúscula")
if not tiene_numero:
    tiene_numero = False
    print("La contraseña debe tener al menos un número")
if not tiene_simbolo:
    tiene_simbolo = False
    print("La contraseña debe tener al menos un símbolo")

if(len(password) >= 8 and tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_simbolo):
    print("Contraseña correcta")
