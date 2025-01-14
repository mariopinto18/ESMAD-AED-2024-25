import os



def lerFicheiroText(fileToRead):
    """
    Lê ficheiro de texto passado como argumento da função
    Pode ser ficheiro de playList, playVideos, playYoutube 
    """
    lista = []
    if os.path.exists(fileToRead):   # Ficheiro existe
        file = open(fileToRead, "r", encoding="utf-8")
        lista = file.readlines()
        file.close()    
    return lista


