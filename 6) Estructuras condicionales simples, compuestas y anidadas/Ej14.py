#14) Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el número es 
#positivo, negativo o nulo (es decir cero)

print("######################################################")
print("\tDesarrollado por Walter Santillan")
print("######################################################")

num = int(input("Ingresar un numero: "))

if num == 0:
    print("El numero es nulo")
else:
    if num > 0:
        print("El numero es positivo")
    else:
        print("El numero es negativo")
