import os 
import random

#  inicializa matriz  com valores aleatorios
def inicializa_matriz():
    """
    Inicializar matriz com dados aleatórios    
    """
    matriz = []
    dim = int(input("\nDimensão da matriz:"))     # dimensão da matriz, nº de linhas / colunas
    for i in range(dim):
        matriz.append([])                         # faz o append de cada sub-lista (ou linha)
        for j in range(dim):                      # preenche cada uma das sub-listas com valores aleatorios
            num = random.randint(10,100)
            matriz[i].append(num)

    print("\n\nMatriz Gerada:")
    for linha in matriz:
        print(linha)     # imprime cada linha / sub-lista da matriz
    input()
    return matriz         # devolve a matriz preenchida com valores aleatórios


# recebe uma lista bidimensional (matriz) e imprime a sua transposta
def transposta(matriz):
    """
    recebe uma matriz e imprime a transposta    
    """
    if matriz == []: 
        print("A matriz está vazia")
        input()
        return

    print("\n\nMatriz Original:")
    for i in range(len(matriz)):
        for j in range (len(matriz)):
            print(matriz[i][j], end = " ")
        print()

    print("\n\nMatriz Transposta:")
    for i in range(len(matriz)):
        for j in range (len(matriz)):
            print(matriz[j][i], end = " ")
        print()
    input()

# determina o maioor valor da matriz / lista bidimensional
def maior_valor(matriz):
    """
    Determina o maior valor de uma matriz    
    """
    if matriz == []:    
        print("A matriz está vazia")
        input()
        return
    listaMax = []    # criar uma lista para adicionar os maximos de cada sub-lista
    for i in range(len(matriz)):
        listaMax.append(max(matriz[i]))     # fazer o append do max de cada sub-lista
    print("O maior valor da matriz é ", max(listaMax))
    input()


# Construção do Menu do programa
op = " "
while op != "0":
    os.system("cls")
    print("\t\tMENU")
    print("1 - Inicializar matriz")
    print("2 - Matriz Transposta")
    print("3 - Maior valor")
    print("0 - Sair")
    op = input("Escolha uma das opções: ")
    if op == "1":
         matriz = inicializa_matriz()
    elif op == "2":
         transposta(matriz)
    elif op == "3":
        maior_valor(matriz)