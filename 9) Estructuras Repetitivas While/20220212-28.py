#28) Desarrollar un programa que permita la carga de 10 valores por teclado 
# y nos muestre posteriormente la suma de los valores ingresados y su promedio.

x = 1
suma = 0 

while x < 10:
    valor = int(input("ingresar 10 valores: "))
    suma = suma + valor
    x = x + 1
    
promedio = suma / 10

print("\nLa suma de los valores es: ", suma)
print("El promedio de los valores es: ", promedio)