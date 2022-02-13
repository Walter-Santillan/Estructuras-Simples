# 31) Se ingresan un conjunto de n alturas de personas por teclado. 
# Mostrar la altura promedio de las personas.

x = 1
suma = 0

n = int(input("Ingresar las alturas por personas: "))

while x <= n:
    alturas = float(input("Ingresar alturas: "))
    suma = suma + alturas

    x = x + 1

promedio = suma / n
print("La altura promedio es: ",promedio)
