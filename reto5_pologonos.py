#Reto 5


"""
Hecer una Unica Funcion para calcular poligonos,
solo uno a la vez, y hacer el calculo de cada poligono (Triangulo, Cuadrado, Retangulo)
"""

def poligonos ():
    poligono= input('¿Que poligono desea calcular: ')
    match poligono:
        case "cuadrado":
            lado =int(input('Digite la medida de un lado en cm: '))            
            area = lado * lado
            print (f'El area de el {poligono} es: {area} cm*2')
            
        case "retangulo":
            base =int(input('Digite la medida de la base en cm: '))
            altura =int(input('Digite la medida de la altura en cm: '))
            area = base * altura
            print (f'El area de el {poligono} es: {area}cm*2')
            
        case "triangulo":
            base =int(input('Digite la medida de la base en cm: '))
            altura =int(input('Digite la medida de la altura en cm: '))
            area = (base * altura)/2
            print (f'El area de el {poligono} es: {area} cm*2')

poligonos()
            
        