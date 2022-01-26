#10) Se ingresan tres notas de un alumno, si el promedio es mayor o igual a siete mostrar un mensaje 
#"Promocionado".
print("######################################################")
print("\tDesarrollado por Walter Santillan")
print("######################################################")
nota1 = int(input("\nIngresar la primera nota: "))
nota2 = int(input("Ingresar la segunda nota: "))
nota3 = int(input("Ingresar la tercer nota: "))

promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 7:
    print("\nEsta promocionado")
else:
    print("No esta promocionado")