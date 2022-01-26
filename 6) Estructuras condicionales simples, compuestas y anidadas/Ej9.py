#9) Realizar un programa que solicite la carga por teclado de dos números, si el primero es mayor al 
# segundo informar su suma y diferencia, en caso contrario informar el producto y la división del 
# primero respecto al segundo.
print("######################################################")
print("\tDesarrollado por Walter Santillan")
print("######################################################")
num1 = int(input("\nIngresar el primer numero: "))
num2 = int(input("Ingresar el segundo numero: "))

if num1 > num2:
    suma = num1 + num2
    diferencia = num1 - num2
    print("\nLa suma de los dos numeros es: ", suma)
    print("La diferencia de los dos numeros es: ", diferencia)
else:
    producto = num1 * num2
    division = num1 / num2
    print("\nEL producto es: ", producto)
    print("La division es: ", division)