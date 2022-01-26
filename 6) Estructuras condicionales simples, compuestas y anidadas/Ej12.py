#12) Confeccionar un programa que pida por teclado tres notas de un alumno, calcule el promedio e 
#imprima alguno de estos mensajes:
#Si el promedio es >=7 mostrar "Promocionado".
#Si el promedio es >=4 y <7 mostrar "Regular".
#Si el promedio es <4 mostrar "Reprobado".

print("######################################################")
print("\tDesarrollado por Walter Santillan")
print("######################################################")

nota1 = int(input("Ingresar la primera nota: "))
nota2 = int(input("Ingresar la segunad nota: "))
nota3 = int(input("Ingresar la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 7:
    print("Esta promocionado/a")
else:
    if promedio >= 4:
        print("Esta regular")
    else:
        print("Esta Reprobado/a")