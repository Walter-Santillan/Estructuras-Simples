#17) Confeccionar un programa que lea por teclado tres números enteros distintos y nos muestre el 
#mayor.

num1 = int(input("Ingresar el primer nuemero entero: "))
num2 = int(input("Ingresar el segundo numero enetro: "))
num3 = int(input("Ingresar el tercer numero entero: "))

if num1 > num2 and num1 > num3:
        print("El primer numero es el mayor")
else:
    if num2 > num3:
        print("El segundo numero es el mayor")
    else:
        print("El tercer numero es el mayor")