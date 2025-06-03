""" 
Pide al usuario:
- Su edad.
- Si tiene licencia de conducir (sí o no).
🔽 Imprime:
- "Puede conducir" → si tiene 18 o más y sí tiene licencia.
- "No puede conducir" → en cualquier otro caso. 
"""

edad = int(input("Ingrese su edad"))
licencia = str(input("Tiene licencia de conducir? Resonda (si/no)"))

if edad >= 18 and licencia == "si":
  print('Usted puede conducir')
else:
  print('No puede conducir')