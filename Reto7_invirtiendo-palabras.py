#Ejercicio 7

#Invirtiendo Cadenas

def reversed_word():
    word = input("Digite una palabra o frace: ")
    flipped_word = [ ]

    for letter in word:
        flipped_word.insert(0, letter)
        
    word_2 = "".join(flipped_word)
    
    print(f"\"{word_2}\" ")
    
reversed_word()
    
