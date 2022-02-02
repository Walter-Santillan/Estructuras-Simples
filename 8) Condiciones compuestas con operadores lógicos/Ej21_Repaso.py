#21) Se ingresan por teclado tres números, si al menos uno de los valores ingresados es menor a 10, 
#imprimir en pantalla la leyenda "Alguno de los números es menor a diez".

num1 = int(input("Ingresar el primer numero: "))
num2 = int(input("Ingresar el segundo numero: "))
num3 = int(input("Ingresar el tercer numero: "))

if num1 < 10 or num2 < 10 or num3 < 10:
    print("Algunos de los numeros es menor a 10")
else:
    print("Ninguno es menor a 10")