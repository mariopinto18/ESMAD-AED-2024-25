from PIL import Image
"""
Criar imagem com uma moldura superior e inferior de 20 pixels, azul
""" 
pathImages = ".\\images\\"                   # caminho da pasta atual de imagens

def imageMoldura(imagem1):
    pixelMap = imagem1.load()                  # load de pixel data (lista bidimensional)

    for i in range(imagem1.width):               # largura
        for j in range(imagem1.height):          #altura
            if i <20 or i >imagem1.width-20:
                pixelMap[i,j] = (255,0,255)      # Azul
            if j <20 or j > imagem1.height-20:   
                pixelMap[i,j] = (255,0,255)   # Azul

        if i > imagem1.width/2-5 and i < imagem1.width/2 +5:
            pixelMap[i,j] = (255,0,255)   # Azul
    return imagem1

imagem1 = Image.open(pathImages+'img1.jpg')
imageMoldura(imagem1)

imagem1.show()
imagem1.save(pathImages+'img1Moldura.jpg')