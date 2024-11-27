from PIL import Image
"""
Criar imagem com uma moldura superior e inferior de 20 pixels, azul
""" 
pathImages = ".\\images\\"                   # caminho da pasta atual de imagens
imagem1 = Image.open(pathImages+'img1.jpg')
pixelMap = imagem1.load()                  # load de pixel data (lista bidimensional)

for i in range(imagem1.width):               # largura
    for j in range(imagem1.height):          #altura
        if i <10 or i >imagem1.width-10:
             pixelMap[i,j] = (0,0,255)      # Azul
        if j <10 or j > imagem1.height-10:   
            pixelMap[i,j] = (0,0,255)   # Azul
        if i > imagem1.width/2-5 and i < imagem1.width/2 +5:
            pixelMap[i,j] = (0,0,255)   # Azul
        if j > imagem1.height/2-5 and j < imagem1.height/2 +5:
            pixelMap[i,j] = (0,0,255)   # Azul

imagem1.show()
imagem1.save(pathImages+'img1Moldura.jpg')