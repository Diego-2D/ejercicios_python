
#nombre de cerveza

#print(('El Nombre de tu cerveza sera:\n') + ('"') + ( (input("¿Que te hace Reir?")+(input("¿Que te hace llorar?") + ('"')))))

#palabra isograma

#palabra= input("Escriba una palabra: ")
#list_palabra = list(palabra.lower())
#verdadera = [ ]
#for letra in list_palabra:
#    if letra in verdadera:
#        print('se repitio la '+ letra)
#       
#    else:
#        verdadera.append(letra)
#        
#if len(verdadera) == len(list_palabra):
#    print(True)
    

# Cuantos digitos tiene un numero

numero = int(input('digite un numero: '))

digitos = 0
while  True:
    if numero / 10 >= 1: 
        digitos += 1
        numero /= 10
    else:
        break
 
print (int(digitos) + 1)

