import os



def escreveTexto(texto):
    """
    Receives a text and write it in a binary file
    """
    fTextBin = open(file, 'wb')
    fTextBin.write(bytes(texto, encoding = "utf-32"))
    fTextBin.close()


def lerTexto():
    """
    returns string with text file 
    """
    fTextBin= open(file, 'rb')
    texto= fTextBin.read()
    fTextBin.close()
    return str(texto, encoding="utf-32")


#-------------------------------
file = ".\\ficheiros\\dados.bin"
pasta = "ficheiros"
if not os.path.exists(pasta):
    os.mkdir(pasta)

texto = "este e um exemplo para a ficha 10"
escreveTexto(texto)   # função que guarda texto em ficheiro binario

input("<enter>")
print(lerTexto())     # Lê texto de ficheiro binário e imprime na consola

