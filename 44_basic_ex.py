"""
Elimina los duplicados de una frase
- Pide una frase al usuario.
- Elimina las palabras que aparecen más de una vez.
Muestra solo las palabras únicas, en el orden original.

Entrada: el sol brilla el sol fuerte
Salida : brilla fuerte

"""

frase = input("Por favor, inserte una frase : \n").lower()
frase = frase.split()
contador = {}
unicas = []

for palabra in frase:
    if palabra in frase:
        contador[palabra] = contador.get(palabra, 0) + 1

for palabra in frase:
    if contador[palabra] == 1:
        unicas.append(palabra)

print(f"Las palabras unicas son : {" ".join(unicas)}")
