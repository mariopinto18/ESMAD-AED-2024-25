
lista = [1,2,3,4,5,6,7,8,9,10]
ficheiro = "teste.bin"
 
# Lê o ficheiro binário com a lista
fileBin = open(ficheiro, "rb")
lista = fileBin.read()   # Lê o fx binário 
novaLista = list(lista)   # converte para uma lista 
fileBin.close()
print(novaLista)


"""
# Guarda lista em ficheiro binário
fileBin = open(ficheiro, "wb")
linhaBin = bytearray(lista)
fileBin.write(linhaBin)
fileBin.close()


# Lê o ficheiro binário com a lista
fileBin = open(ficheiro, "rb")
lista = fileBin.read()   # Lê o fx binário 
novaLista = list(lista)   # converte para uma lista 
fileBin.close()
print(novaLista)
"""