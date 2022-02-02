#25) Escribir un programa en el cual: dada una lista de tres valores numéricos distintos se calcule e 
#informe su rango de variación (debe mostrar el mayor y el menor de ellos).

print("######################################################")
print("\tDesarrollado por Walter Santillan")
print("######################################################")

num1 = int(input("\nIngresar el primer numero: "))
num2 = int(input("Ingresar el segundo numero: "))
num3 = int(input("Ingresar el tercer numero: "))

#IMPRIMO EL MENOR
if num1 < num2 and num1 < num3:
    print(num1)
else:
    if num2 < num3:
        print(num2)
    else:
        print(num3)
        
#IMPRIMO EL MAYOR
if num1 > num2 and num1 > num3:
    print(num1)
else:
    if num2 > num3:
        print(num2)
    else:
        print(num3)