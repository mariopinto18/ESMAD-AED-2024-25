# função que recebe um texto e devolve o primeiro e último nome 
def shortName(nome):
    """
    function recebe um nome e devolve apenas o primeiro nome contactano co o último
    Args: string
    Returns: string
    """
    nomeAbrev = ""
    pos = nome.find(" ")                    # procura o 1º espaço
    if pos != -1:
        primeiroNome = nome[:pos]           # obtém o 1º nome (até ao espaço)
        pos = nome.rfind(" ")               # procura o último espaço
        if pos != -1:
            ultimoNome = nome[pos+1:]       # Obtém o último nome (do espaço até ao fim)
            nomeAbrev = primeiroNome+" " + ultimoNome
            return nomeAbrev
    return "nome inválido"     # no caso de não ter feito o return  na linha anterior


nome = input("Nome:")
print(shortName(nome))


