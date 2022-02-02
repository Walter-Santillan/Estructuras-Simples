#21) Se ingresan por teclado tres números, si al menos uno de los valores ingresados es menor a 10, 
#imprimir en pantalla la leyenda "Alguno de los números es menor a diez".

print("######################################################")
print("\tDesarrollado por Walter Santillan")
print("######################################################")

print("\nSe ingresan por teclado los tres números")
num1 = int(input("Ingresar el primer número: "))
num2 = int(input("Ingresar el segundo número: "))
num3 = int(input("Ingresar el tercer número: "))

if num1 < 10 or num2 <10 or num3 < 10:
    print("\nAl menos uno de los números es menor a diez")
else:
    print("\nLos números no son menores a diez")