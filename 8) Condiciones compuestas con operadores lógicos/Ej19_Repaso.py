#19) Realizar un programa que pida cargar una fecha cualquiera, luego verificar si dicha fecha 
#corresponde a Navidad.

dia = int(input("Ingresar dia: "))
mes = int(input("Ingresar mes: "))
año = int(input("Ingresar año: "))

if dia == 25 and mes == 12:
    print("Es navidad")
else:
    print("No es Navidad")