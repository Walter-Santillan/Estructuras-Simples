#22) Se ingresan tres valores por teclado, si todos son iguales se imprime la suma del primero con el 
#segundo y a este resultado se lo multiplica por el tercero.

print("######################################################")
print("\tDesarrollado por Walter Santillan")
print("######################################################")

print("\nSe ingresan los números")
num1 = int(input("Ingresar el primer número: "))
num2 = int(input("Ingresar el segunro número: "))
num3 = int(input("Ingresar el tercer número: "))

if num1 == num2 and num1 == num3:
    suma = num1 + num2
    print("\nLa suma es: ", suma)
    producto = suma * num3
    print("\nLa suma del primer número y el segundo número multiplicado por el tercer número es:", producto)
else:
    print("\nNo se puede realizar la operación, todos los números son distintos")