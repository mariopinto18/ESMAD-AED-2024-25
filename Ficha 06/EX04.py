from PIL import Image
"""
Criar imagem com uma moldura superior e inferior de 20 pixels, azul
""" 
pathImages = ".\\images\\"                   # caminho da pasta atual de imagens

imagem1 = Image.open(pathImages+'img2.jpg')
def imageGrayScale(imagem1):
    pixelMap = imagem1.load()                  # load de pixel data (lista bidimensional)

    for i in range(imagem1.width):               # largura
        for j in range(imagem1.height):          #altura
            p = pixelMap[i,j]                   # pixel expecífico 
            red= p[0]                           # RGB de vermelho
            green = p[1]                        # RGB de verde
            blue = p[2]                         # RGB de azul
            red = green = blue = int((0.299* red + 0.587*green + 0.114*blue) / 3)
            pixelMap[i,j] = (red, green, blue)  # Forma mais simples de grayScale
        
    imagem1.show()
    imagem1.save(pathImages+'grayScale.jpg')

imagem1 = Image.open(pathImages+'img2.jpg')
imageGrayScale(imagem1)
