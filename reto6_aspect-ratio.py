"""
Ejercicio 6 sacar el Aspect ratio de una imagen
"""
from PIL import Image

#Importacion de imagen
ruta = "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"
img =  Image.open (ruta)

#extraccion de alto y ancho de la imagen
a = img.height 
b = img.width
 
def ratio_of_picture (h, w):
    
    for n in range (2,100):
      if h % n == 0 and w % n == 0:
        h /= n
        w /= n
        
      else:
          print(f"ratio = {int(h)}:{int(w)}")
          break
 
        
    
ratio_of_picture(a , b)
       