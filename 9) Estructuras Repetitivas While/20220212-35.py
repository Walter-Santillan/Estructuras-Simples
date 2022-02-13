#35) Realizar un programa que permita cargar dos listas de 15 valores cada una. 
# Informar con un mensaje cual de las dos listas tiene un valor acumulado mayor 
# (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
# Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.

suma1 = 0
suma2 = 0
x = 1
print("Carga de la primera lista")
while x <= 15:
    valor = int(input("Ingresar valor: "))
    suma1 = suma1 + valor
    x = x + 1

x = 1
print("Carga de la segunda lista")
while x <= 15:
    valor = int(input("Ingresar valor: "))
    suma2 = suma2 + valor
    x = x + 1

if suma1 > suma2:
    print("La lista 1 es mayor")
else:
    if suma2 > suma1:
        print("La lista 2 es mayor")
    else:
        print("Las lista son iguales")
    