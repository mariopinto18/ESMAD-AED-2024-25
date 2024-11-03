
def countText(texto):
    """
    Recebe um texto e imprime o nº de caracteres, de vogais e de espaços contidos nesse texto
    Args: string
    """
    vogais=0
    comp = len(texto)           # nº de caracteres do texto
    for i in range(0,comp):     # percorre o texto, caracter a caracter, contando as vogais
        if texto[i].lower() == "a" or texto[i].lower() == "e" or texto[i].lower() == "i" or texto[i].lower() == "o" or texto[i].lower() == "u":
            vogais+=1
    # contar espaços
    espacos= texto.count(" ")

    print("Nº de caracteres:", len(texto))
    print("Nº de vogais    :", vogais)
    print("Nº de espaços   :", espacos)



# EX02
texto = input("Indique um texto:")
countText(texto)

