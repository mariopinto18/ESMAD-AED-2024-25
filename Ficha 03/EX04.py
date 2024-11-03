# Função que substitui 2 ou mais espaços por um único espaço
def removeSpaces(texto):
    """
    A função recebe uma string  e substitui sequências de 2 ou mais espaços por um +unico espaço
    Args: texto-string
    """
    while texto.find("  ")!= -1 :          # Enquanto encontrar sequências de 2 espaços
        texto = texto.replace("  ", " ")    # substituir 2 espaços por 1
    print("\nTexto:",texto)


texto = input("Insira um Texto:") 
removeSpaces(texto)

