#Reto 4

"""
Comprobar si un numero es primo o no lo es.
despues imprimir tos los numeros del 1 al 100 que sean primos.
"""

def primos (numero):
    if numero % 2 == 0:
        print(f'El numero {numero} es par.')
    else:
        print(f'El numero {numero} es primo.')
   
    lisata_de_primos =   [ ] #La lista es solo para que se impriman los numeros de forma mas ordenada
    for n in range (0,101):
        if n % 2 == 0:
            pass
        else:
            lisata_de_primos.append(n)
            
    print (lisata_de_primos)
            
primos(15)