from PIL import Image
"""
Cria uma imagem de 240x240 pixels
"""
pathImages = ".\\images\\"          # Opcional: caminho da pasta atual de imagens

newSize = (240, 240) # Tuplo com largura (width) e altura (height) da imagem
imagem = Image.new(size=newSize, mode = "RGB", color= "white")  # Nova imagem

pixelMap= imagem.load()             # "loads" the pixel para uma lista bidimensional
for i in range(imagem.width):       # LARGURA
    for j in range(imagem.height):  # ALTURA
        if i <80:
            pixelMap[i,j] = (0, 0, 255)          # Azul
        elif i < 160:       
            pixelMap[i,j] = (255, 255, 255)     # Branco
        else:
            pixelMap[i,j] = (255, 0, 0)         # Vermelho
imagem.show()                           # mostra a imagem
imagem.save(pathImages+'bandeira.jpg')     # Grava imagem no ficheio pretendido