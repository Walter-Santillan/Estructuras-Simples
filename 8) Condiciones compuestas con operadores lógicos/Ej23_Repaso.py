#23) Escribir un programa que pida ingresar la coordenada de un punto en el plano, es decir dos 
# valores enteros x e y (distintos a cero).

# Posteriormente imprimir en pantalla en que cuadrante se ubica dicho punto. (1º Cuadrante si x > 0 Y 
# y > 0 , 2º Cuadrante: x < 0 Y y > 0, etc.).

x = int(input("Ingresar un numero distinto de cero: "))
y = int(input("Ingresar otro numero distinto de cero: "))

if x > 0 and y > 0:
    print("1er cuadrante")
else:
    if x < 0 and y > 0:
        print("2do cuadrante")
    else:
        if x < 0 and y < 0:
            print("3er cuadrante")
        else:
            if x > 0 and y < 0:
                print("4to cuadrante")
            else:
                print("ningun cuadrante")

