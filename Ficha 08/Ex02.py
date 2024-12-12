import os



def lerFicheiro():
    """
    return text file, codified by cifra cesar
    """
    fileTexto = open(ficheiro, "r", encoding="utf-8")
    textoCodificado = fileTexto.read()
    fileTexto.close() 
    return textoCodificado


def decript(textoCodificado):
    """
    Decodes string text
    """
    texto= ""
    for char in textoCodificado:
        posicaoASCII = ord(char)
        novocaracter = chr(posicaoASCII - chave)
        texto+= novocaracter
    return texto


def encript(texto, chave):
    """
    it reveives a string and a key (Cifra Cesar)
    """
    textoCodificado= ""
    for char in texto:
        posicaoASCII = ord(char)
        novocaracter = chr(posicaoASCII+ chave)
        textoCodificado+= novocaracter
    return textoCodificado


def guardaFicheiro(textoCodificado):
    fileTexto = open(ficheiro, "w", encoding="utf-8")
    fileTexto.write(textoCodificado)
    fileTexto.close()
    print("Texto guardao em ficheiro...")
    input()


#-----------------------------------------
ficheiro = ".\\ficheiros\\test.txt"
pasta = "ficheiros"
chave = 3
if not os.path.exists(pasta):
    os.mkdir(pasta)


op = "1"
while op != "0":
    os.system("cls")
    print("\n\nMENU")
    print("1 - Escrever em ficheiro")
    print("2 - Ler ficheiro")
    print("0 - Sair")
    op = input("\t opção: ")
    if op =="1":
        texto = input("Texto: ")
        textoCodificado= encript(texto, chave)  
        guardaFicheiro(textoCodificado)
    elif op=="2":           
        textoCodificado = lerFicheiro()
        print("Texto descodificado:", decript(textoCodificado))
        input()
        

