#2) Realizar la carga del precio de un producto y la cantidad a llevar. Mostrar cuanto se debe pagar 
#(se ingresa un valor entero en el precio del producto).

print("###############################################")
print("\tDesarrollado por Best-Seller")
print("###############################################")

precio = int(input("Ingresar el precio del producto: "))
cantidad = int(input("Ingresar la cantidad a llevar: "))

totalPagar = precio * cantidad

print("\nEl importe total a pagar es: ", totalPagar)