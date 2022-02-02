#25) Escribir un programa en el cual: 
# dada una lista de tres valores numéricos distintos se calcule e informe 
# su rango de variación (debe mostrar el mayor y el menor de ellos).

num1 = int(input("Ingresar el primer valor: "))
num2 = int(input("Ingresar el segundo valor: "))
num3 = int(input("Ingresar el tercer valor: "))

if num1 < num2 and num1 < num3:
        print(num1)
else:
    if num2 < num3:
        print(num2)
    else:
        print(num3)
print("a")        
if num1 > num2 and num1 > num3:
    print(num1)
else:
    if num2 > num3:
        print(num2)
    else:
        print(num3)

