# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 22:48:07 2022

@author: Best-Seller
"""


"""
MIDIENDO CADENAS DE TEXTOS.
"""

palabras = ['gato', 'ventana', 'defenestrado']
for p in palabras:
    print(p, len(p))

#HACER UNA COPIA POR SUBCADENA.

for p in palabras[:]:
    if len(p) > 6:
        palabras.insert(0, p)

#IMPRIME LOS NUMEROS (0 HASTA EL 4). 
print("")        
for numeros in range(5):
    print(numeros)
    
#IMPRIME LOS NUMEROS (5 HASTA EL 9). 
print("")
for numeros in range(5, 10):
    print(numeros)
    
#IMPRIME LOS NUMEROS (0 HASTA EL 8 de 2 en 2).
print("")
for numeros in range(0, 10, 2):
    print(numeros)
    
print("")
for numeros in range(-10, -100, -30):
    print(numeros)
    
#UTILIZAR RANGE Y LEN COMBINADOS.
print("")
a = ['Mary', 'tenia', 'un', 'corderito']
for i in range(len(a)):
    print(i, a[i])
    
#CONSTRUIR UNA LISTA CON LA FUNCIÓN "list", QUE CREA LISTAS A 
#PARTIR DE OBJETOS ITERABLES.

list (range(5))