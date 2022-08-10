print('\n')

print('\tIngresar dos cadenas de caracteres\n')
cadena_1 = input('Dame la primera cadena: ')
cadena_2 = input('Dame la segunda cadena: ')
print("\n")
print( cadena_2[:2] + cadena_1[2:] + "" "" + cadena_1[:2] + cadena_2[2:])

print('\n')

print('\tMostrar si una cadena de caracteres es un palindromo\n')
cadena_3 = input('Dame una cadena: ')
cadena_al_reves = cadena_3[: : -1]
print(cadena_al_reves)

if (cadena_3 == cadena_al_reves):
    print('Es un palindromo')
else:
    print('No es un palindromo')