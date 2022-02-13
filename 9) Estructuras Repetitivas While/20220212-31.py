# 31) Se ingresan un conjunto de n alturas de personas por teclado. 
# Mostrar la altura promedio de las personas.

print("###############################################")
print("########\tWalter Santillán    ###########")
print("###############################################")

print("\n1Analizando alturas")
x = 1
suma = 0

n = int(input("\nIngresar las alturas por personas: "))

while x <= n:
    alturas = float(input("Ingresar alturas: "))
    suma = suma + alturas

    x = x + 1

promedio = suma / n
print("\nLa altura promedio es: ",promedio)
