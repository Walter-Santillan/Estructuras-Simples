#23) Escribir un programa que pida ingresar la coordenada de un punto en el plano, es decir dos 
#valores enteros x e y (distintos a cero).
#Posteriormente imprimir en pantalla en que cuadrante se ubica dicho punto. (1º Cuadrante si x > 0 Y 
#y > 0 , 2º Cuadrante: x < 0 Y y > 0, etc.).

print("######################################################")
print("\tDesarrollado por Walter Santillan")
print("######################################################")

print("\nSe ingresan las coordenadas")
x = int(input("Ingresar coordenada en x: "))
y = int(input("Ingresar coordenada en y: "))

if x > 0 and y > 0:
    print("Primer cuadrante")
else:
    if x < 0 and y > 0:
        print("Segundo cuadrante")
    else:
        if x < 0 and y < 0:
            print("Tercer cuadrante")
        else:
            if x > 0 and y < 0:
                print("Cuarto cuadrante")
            else:
                print("Esta sobre el origen")