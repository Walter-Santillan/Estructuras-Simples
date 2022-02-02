#20) Se ingresan por teclado tres números, si todos los valores ingresados son menores a 10, 
#imprimir en pantalla la leyenda "Todos los números son menores a diez".

print("######################################################")
print("\tDesarrollado por Walter Santillan")
print("######################################################")

print("\nSe ingresan por teclado los tres números")
num1 = int(input("Ingresar el primer número: "))
num2 = int(input("Ingresar el segundo número: "))
num3 = int(input("Ingresar el tercer número: "))

if num1 and num2 and num3 < 10:
    print("\nTodos los números son menores a diez")
else:
    print("\nTodos los números no son menores a diez")