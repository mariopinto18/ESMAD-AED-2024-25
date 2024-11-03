def standardName(nome):
    """
    function receives a string text and returns the firt name, last name and 
    initials of middle names
    Args:  string
    Returns: string
    """
    nomeAbrev=""
    # --------- primeiro nome --------------------
    pos = nome.find(" ")               # procura o 1º espaço
    if pos != -1:
        nomeAbrev = nome[:pos]         # obtem primeiro nome (até espaço)
    else:
        return "nome inválido!"
    
# --------- Iniciais dos nomes intermédios
    for i in range(nome.find(" "), nome.rfind(" ")):
        if nome[i] == " ":
            nomeAbrev+= " " + nome[i+1]+ "."

# ---------  ultimo nome ------------------
    pos = nome.rfind(" ")                   # procura o último espaço 
    if pos != -1:
        nomeAbrev+= " " + nome[pos+1:]       # obtem o ultimo nome
    
    return nomeAbrev


nome = input("Indique um nome:")
print(standardName(nome))
