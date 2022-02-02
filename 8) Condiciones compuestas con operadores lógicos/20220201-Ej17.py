#17) Confeccionar un programa que lea por teclado tres números enteros distintos y nos muestre el 
#mayor.

print("######################################################")
print("\tDesarrollado por Walter Santillan")
print("######################################################")

print("\nSe ingresan los números")
num1 = int(input("Ingresar el primer número: "))
num2 = int(input("Ingresar el segundo número: "))
num3 = int(input("Ingresar el tercer número: "))


if num1 > num2 and num1 > num3:
    print("\nEl mayor es el primer número")
else:
    if num2 > num3:
        print("\nEl mayor es el segundo número")
    else:
        print("\nEl mayor es el tercer número:")
  