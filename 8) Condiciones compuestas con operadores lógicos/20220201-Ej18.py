#18) Se carga una fecha (día, mes y año) por teclado. Mostrar un mensaje si corresponde al primer 
#trimestre del año (enero, febrero o marzo) Cargar por teclado el valor numérico del día, mes y año. 
#Ejemplo: dia:10 mes:2 año:2018.

print("######################################################")
print("\tDesarrollado por Walter Santillan")
print("######################################################")

print("\nSe ingresan el día, mes y el año")
dia = int(input("Ingresar dia: "))
mes = int(input("Ingresar mes: "))
año = int(input("Ingresar año: "))

if mes == 1 or mes == 2 or mes == 3:
    print("\nCorresponde al primer trimestre")
else:
    print("\nNo corresponde al primer trimestre")