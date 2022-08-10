print('\n')
print('Generar aleatoriamente un valor y el usuario debe adivinarlo')

from random import *

def generaNumeroAleatorio(minimo, maximo):
    return randint(minimo, maximo)

numero_buscado = generaNumeroAleatorio(1, 100)
encontrado = False
intentos = 0

while not encontrado:
    numeroUsuario = int(input('\nIntroducir el numero buscado: '))
    if numeroUsuario > numero_buscado:
        print('El numero que buscas es menor')
        intentos = intentos + 1
    elif numeroUsuario < numero_buscado:
        print('El numero que buscas es mayor')
        intentos = intentos + 1
    else:
        encontrado = True
        print('Has acertado, el numero correcto es: ', numeroUsuario, 'te ha llevado', intentos, 'intentos')
    


