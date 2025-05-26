#Reto 3 
#Dificil

def fibonacci ():
    numero1 = 0
    numero2 = 1
    suma = 0
    
    while suma <= 100:
 
        if suma == 0:
            print(numero1)
            suma = numero1 + numero2
            print(numero2)
            numero1 = numero2
            numero2 = suma
            
            
        else:
             print(suma)
             suma = numero1 + numero2
             numero1 = numero2
             numero2 = suma
        
fibonacci()
    
    