""" Pide un número entero y muestra su tabla de multiplicar del 1 al 10, usando un bucle. """

numero = int(input("Ingrese un numero entero para ver su tabla de multiplicar del 1 al 10\n"))
multi = 1
while multi <= 10:
    resultado = numero * multi
    print(f'{numero}*{multi} = {resultado}')
    multi += 1