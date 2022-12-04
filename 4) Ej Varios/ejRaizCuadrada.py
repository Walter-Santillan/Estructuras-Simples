import math

print("\n\tPROGRAMA QUE CALCULA LA RAIZ CUADRADA DE UN NUMERO")

numero = int(input("Introduce un numero por favor: "))
intentos = 0

while numero < 0:
    print("\nNo se puede hallar la raiz de un numero negativo.")
    
    numero = int(input("Vuelva a introducir un numero por favor: "))
    if numero < 0:
        intentos = intentos + 1
    
    if intentos == 2:
        print("\nHas consumido demasiados intentos, el programa ha finalizado.")
        break;

if intentos < 2:
    solucion = math.sqrt(numero)
    print("\nLa raiz cuadrada de " + str(numero) + " es: " + str(solucion))