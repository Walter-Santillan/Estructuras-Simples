#15) Confeccionar un programa que permita cargar un número entero positivo de hasta tres cifras y 
#muestre un mensaje indicando si tiene 1, 2, o 3 cifras. Mostrar un mensaje de error si el número de 
#cifras es mayor.

print("######################################################")
print("\tDesarrollado por Walter Santillan")
print("######################################################")

num = int(input("Ingresar un numero entero positivo entre 1 y 999: "))

if num < 10:
    print("El numero tiene una cifra")
else:
    if num < 100:
        print("El numero tiene dos digitos")
    else:
        if num < 1000:
            print("El numero tiene tres digitos")
        else:
            print("Error en la entrada de datos, vuelva a intentar")

