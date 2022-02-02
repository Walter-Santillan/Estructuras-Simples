#20) Se ingresan por teclado tres números, si todos los valores ingresados son menores a 10, 
#imprimir en pantalla la leyenda "Todos los números son menores a diez".

num1 = int(input("Ingresar el primer numero: "))
num2 = int(input("Ingresar el segundo numero: "))
num3 = int(input("Ingresar el tercer numero: "))

if num1 < 10 and num2 < 10 and num3 < 10:
    print("Todos los numeros son menores a 10")
else:
    print("No son menores a 10")