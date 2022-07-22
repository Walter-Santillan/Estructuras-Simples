# NUMEROS PRIMOS.

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'es igual a', x, '*', n/x)
            break
    else: #ESTE ELSE PERTENECE AL for, NO AL if
        print("")
        print(n, 'es un numero primo')
print("")

# NUMERO PAR.
print("##################################################")
print("")

for num in range(2, 10):
    if num % 2 == 0:
        print('Encontre un numero par', num)
        continue
    print('Encontre un numero', num)
        

