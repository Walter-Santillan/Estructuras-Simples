#22) Se ingresan tres valores por teclado, si todos son iguales se imprime la suma del primero con el 
#segundo y a este resultado se lo multiplica por el tercero.

num1 = int(input("Ingresar el primer valor: "))
num2 = int(input("Ingresar el segundo valor: "))
num3 = int(input("Ingresar el tercer valor: "))

if num1 == num2 == num3:
    suma = num1 + num2
    resultado = suma * num3
    print("La suma del primer y segundo numero es: ", suma)
    print("La suma del primer nuemro y del segundo multiploicado por el tercer numero es: ", resultado)
else:
    print("No se puede realizar la operacion son todos los numeros distintos")