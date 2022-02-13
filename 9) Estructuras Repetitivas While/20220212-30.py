#30) Escribir un programa que solicite ingresar 10 notas de 
# alumnos y nos informe cuántos tienen notas mayores o 
# iguales a 7 y cuántos menores.

print("###############################################")
print("########\tWalter Santillán    ###########")
print("###############################################")

print("Programa que solicita las notas de les alumnes\n")

x = 1
notasAltas = 0
notasBajas = 0

while x <= 10:
    notas = int(input("Ingresar notas: "))
    if notas >= 7:
        notasAltas = notasAltas + 1
    else:
        notasBajas = notasBajas + 1
    x = x + 1
print("\nLa cantidad de notas mayores o igulaes a 7 es: ", notasAltas)
print("La cantidad de notas menores o igulaes a 7 es: ", notasBajas)


