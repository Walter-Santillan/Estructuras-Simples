#19) Realizar un programa que pida cargar una fecha cualquiera, luego verificar si dicha fecha 
#corresponde a Navidad.

print("######################################################")
print("\tDesarrollado por Walter Santillan")
print("######################################################")

print("\nSe ingresan por teclado día, mes y año")
dia = int(input("Ingresar dia: "))
mes = int(input("Ingresar mes: "))
año = int(input("Ingresar año: "))

if dia == 25 and mes == 12:
    print("\nEs Navidad")
else:
    print("\nNo es Navidad")
