"""
Escribe un programa que:
- Pida al usuario su edad.
- Si tiene menos de 18 años, imprima "Menor de edad".
- Si tiene entre 18 y 65, imprima "Adulto".
- Si tiene más de 65, imprima "Adulto mayor".
"""

edad = int(input('Ingrese su edad :'))

if edad < 18:
    print('Es menor de edad')
elif 18 <= edad <= 65:
    print('Es adulto')
else:
    print('Es adulto mayor')
