from PIL import Image
import random

"""
Cria uma imagem de 400x400 pixels
"""
pathImages = ".\\images\\"          # Opcional: caminho da pasta atual de imagens
width = 400
height=400

def ImageArt():
    newSize = (width, height) # Tuplo com largura (width) e altura (height) da imagem
    imagem = Image.new(size=newSize, mode = "RGB", color= "white")  # Nova imagem

    pixelMap= imagem.load()             # "loads" the pixel para uma lista bidimensional
    for i in range(imagem.height):
        for j in range(imagem.width):
            red = random.randint(0,255)
            green = random.randint(0,255)
            blue = random.randint(0,255)
            pixelMap[i,j] = (red, green, blue)        
    imagem.show()                           # mostra a imagem
    imagem.save(pathImages+'imageArt.jpg')     # Grava imagem no ficheio pretendido

ImageArt()