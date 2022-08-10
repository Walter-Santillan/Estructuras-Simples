print('\n')
print('\t<< JUGAR CON RANGOS >>\n')
print('Generar rango de diez números entre 0 y 10:')
print('\n')

rango = list( range(10))
print(rango)

print('\n#########################################################')

print('\n')
print('Generar rango de cinco valores entre 5 y 10:')
print('\n')

rango = list( range(5, 10))
print(rango)

print('\n')
print('#########################################################\n')
print('Generar rango de números decrecientes.\n')

rango = list(range(10, 0, -1))
print(rango)

print('\n')
print('##########################################################\n')
print('Generar dos rangos separados y luego concatenarlos.\n')

rango_1 = list(range(0, 11))
rango_2 = list(range(15, 21))
sumarRangos = rango_1 + rango_2
print(sumarRangos)

print('\n')
print('##########################################################\n')
print('Solicitar nombre del usuaria/o y luego generar rango desde 0\n hasta la longitud de su nombre\n')

nombre = input('¿Como te llamas? ->  ')
rango = list( range(0, len(nombre)))
print(rango)

print('\n')
print('########################################################\n')
print('<< PROGRAMA DESARROLLADO POR WALTER SANTILLAN >>\n')
print('########################################################\n')