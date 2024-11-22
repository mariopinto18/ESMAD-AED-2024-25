def invert(lista):
    """
    recebe uma lista bidimensional (matriz) e imprime a sua transposta    
    """
    print("\n\nMatriz Original:")
    for i in range(len(lista)):             # percorrer cada uma das sub-listas (LINHAS)
        for j in range (len(lista)):
            print(lista[i][j], end = " ")   # imprime posições de sub-lista (COLUNAS)
        print()                             # No final de uma sub-lista (LINHA), força um enter

    print("\n\nMatriz Transposta:")
    for i in range(len(lista)):
        for j in range (len(lista)):
            print(lista[j][i], end = " ")      # matriz transposta consiste em trocar as linhas pelas colunas
        print()



def cria_lista(nlin, ncol):
    """ 
    função que cria uma lista bidimensional com dimensão de  nlin e ncol
    """
    lista = []                      # inicializa lista
    for i in range(nlin):           # percorre as 3 linhas (ou sub-listas)
        lista.append([])            # acrescenta uma lista vazia para cada linha
        for j in range(ncol) :      # percorre as 3 colunas de cada sub-lista
            numero = int(input("Linha {0}, coluna {1} : " .format(i+1,j+1)))
            lista[i].append(numero)         # em cada linha, acrescenta uma coluna à lista
    return lista


lista = cria_lista(3,3)   # Ler lista / matriz
invert(lista)             # Função que imprime a transposta


