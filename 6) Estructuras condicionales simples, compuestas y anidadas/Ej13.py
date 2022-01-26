#13) Se cargan por teclado tres números distintos. Mostrar por pantalla el mayor de ellos.

print("######################################################")
print("\tDesarrollado por Walter Santillan")
print("######################################################")

num1 = int(input("Ingresar el primer valor: "))
num2 = int(input("Ingresar el segundo valor: "))
num3 = int(input("Ingresar el tercer valor: "))

if num1 > num2:
    if num1 > num3:
        print("El mayor es el primer valor")
    else:
        print("El mayor es el tercer valor")
else:
    if num2 > num3:
        print("El mayor es el segundo valor")
    else:
        print("El mayor es el tercer valor")
    