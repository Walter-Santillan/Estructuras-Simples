#32) En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, 
# realizar un programa que lea los sueldos que cobra cada empleado e informe 
# cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300. 
# Además el programa deberá informar el importe que gasta la empresa en sueldos al personal.

print("###############################################")
print("########\tWalter Santillán    ###########")
print("###############################################")

print("\nAnalizando sueldos de les empleades")

x = 1
cont1 = 0 #contador de empleados que cobran entre 100 y 300. 
cont2 = 0 #contador de empleados que cobran mas de 300.
gastoSueldos = 0 #acumulamos los suledos.

n = int(input("\nIngresar la cantidad de empleados: "))

while x <= n:
    sueldos = float(input("Ingresar los sueldos de cada empleado: "))
    if sueldos <= 300:
        cont1 = cont1 + 1
    else:
        cont2 = cont2 + 1
    gastoSueldos = gastoSueldos + sueldos
    x = x + 1

print("\nLos empleados que cobran entre 100 y 300 es: ", cont1)
print("Los empleados que cobran mas de 300 es: ", cont2)
print("El importe que gasta la empresa en sueldos es. ", gastoSueldos)
