#29) Una planta que fabrica perfiles de hierro posee un lote de n piezas.
# Confeccionar un programa que pida ingresar por teclado la cantidad de 
# piezas a procesar y luego ingrese la longitud de cada perfil; sabiendo 
# que la pieza cuya longitud esté comprendida en el rango de 1.20 y 1.30 son aptas. 
# Imprimir por pantalla la cantidad de piezas aptas que hay en el lote.

x = 1
cantPiezasAptas = 0

cantPiezasProcesar = int(input("Ingresar la cantidad de piezas a procesar: "))

while x <= cantPiezasProcesar:
    longitud = float(input("Ingresar la longitud de cada perfil: "))
    if longitud >= 1.20 and longitud <= 1.30:
        cantPiezasAptas = cantPiezasAptas + 1
    x = x + 1


print("La cantidad de peizas aptas son: ", cantPiezasAptas) 

