#Reto 2

#Anagrama

palabra1 = input('Escriba una Palabra: ')
palabra2 = input ('Esceiba una segunda palabra: ')

def anagrama (word1, word2):
    
    lista_1 = list(word1.lower())
    lista_2 = list(word2.lower())
    anagrama_list =[]
   
    for letra in lista_1:
         
        if letra in  lista_2:
            anagrama_list.append(letra)
            
    if len(anagrama_list) == len(lista_2):
            print (True)
            
        
    else:
      print (False)
      
anagrama(palabra1,palabra2)
    