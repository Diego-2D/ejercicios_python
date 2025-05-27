# Reto 1
"""
Hacer un programa que genere una secuencia de el 1 al 100,
los multipos de 3 se remplazaran por la palabra 'fizz ',
si es multilpo de 5 se replazara por la palabra 'bizz'
si ed multiplo de las dos se replazara por 'fizzbizz'
"""
def fizzbuzz ():
    for n in range(1, 101):
                     if n%3 ==0 and n%5 == 0:
                         print('fizz bizz')
                         
                     elif n%3 == 0:
                         print ('fizz')
                     
                     elif n%5 == 0:
                         print ('bizz') 
                           
                     else:
                          print(n)
                          
            
fizzbuzz ()