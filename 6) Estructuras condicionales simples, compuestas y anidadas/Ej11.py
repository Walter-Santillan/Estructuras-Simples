#11) Se ingresa por teclado un número positivo de uno o dos dígitos (1..99) mostrar un mensaje 
#indicando si el número tiene uno o dos dígitos.
#(Tener en cuenta que condición debe cumplirse para tener dos dígitos un número entero).
print("######################################################")
print("\tDesarrollado por Walter Santillan")
print("######################################################")
valor = int(input("\nIngresar un valor comprendido entre 1 y 99: "))

if valor > 10:
    print("\nTiene dos digitos")
else:
    print("\nTiene un digito")