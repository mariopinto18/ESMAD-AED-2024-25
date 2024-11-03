# Função que recebe um texto e verifica se é capicua ou não
def capicua(texto):
    """
    Recebe um texto e devolve um valor booleano: True se for capicua. False caso náo seja
    Args: texto, string
    Returns: booleano, True ou False
    """

    # Solução alternativa
    if texto[:] == texto[::-1]:
       return True
    else:
        return False
    #Outra solução (mais algoritmica)
    invTexto = "" 
    for i in range (len(texto)-1, -1, -1):   # ciclo for que percorre todos os caracteres do último até à posição 0
        invTexto+= texto[i]

    if texto == invTexto:
        return True
    else:
        return False


texto = input("\tInsira um texto: ")
if capicua(texto.lower()) == True:
    print("\t{0} é capicua" .format(texto))
else:
    print("\t{0} não é capicua" .format(texto))


