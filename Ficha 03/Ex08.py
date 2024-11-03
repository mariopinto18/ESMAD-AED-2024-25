#reverseWords - recebe um texto e inverte a ordem das palavras
def reverseWords(text):
    """
    Recebe uma string (texto) 
    e devolve o mesmo texto, com as palavras por ordem inversa
    Args: string
    Returns: string
    """
    newText=""
    pos = text.rfind(" ")                # procura o último espaço
    while pos != -1:            
        newText+= text[pos+1:] + " "     # novo texto inclui caracteres da posição a seguir ao espaço até ao fim
        text=text[0:pos]                 # redefine o texto: do início até ao espaço encontrado anteriormente
        pos = text.rfind(" ")            # procura agora o ultimo espalo no texto "que sobra"
    newText+=text
    return newText

text = input("Texto:")
print(reverseWords(text))

