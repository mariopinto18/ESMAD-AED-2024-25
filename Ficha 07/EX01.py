import os

listaContinentes = ["Europa", "America", "Africa", "Asia", "Oceania"]


def lerFicheiro():
    """
    ler ficheiro de paises e devolve uma lista com o conteudo do fx
    """
    filePaises = open(ficheiro, 'r')
    listaPaises = filePaises.readlines()
    filePaises.close()
    return listaPaises


def guardarFicheiro(pais, continente):
    filePaises = open (ficheiro, "a", encoding="utf-8")
    linha = pais + ";" + continente + "\n"
    filePaises.write(linha)
    filePaises.close()


def inserePais():
    """
    Lê pais e lê um continente e acrescenta ao ficheitro paises.txt
    """
    os.system('cls')
    pais = input("\n\n\t\tIndique o país       : ")
    continente = input("\n\n\t\tIndique o  continente: ")
    if continente not in listaContinentes:
        print("O continente não existe")
        input()
    else:
        listaPaises = lerFicheiro()
        for linha in listaPaises:
            campos = linha.split(";")
            if campos[0] == pais:
                print("O pais {:s} já existe" .format(pais))
                input()
                return
        guardarFicheiro(pais, continente)

#----------------------------------------------------------
def consultaPaises():
    os.system('cls')
    print("\n\n\t     Países          Continente")
    print("\n\n\t---------------------------------")
    listaPaises = lerFicheiro()
    for linha in listaPaises:
        listaPosicao = linha.split(";")
        if len(listaPosicao[0]) <=6:
            listaPosicao[0]+= "\t"
        print("\t",listaPosicao[0],"\t\t", listaPosicao[1])
    input()

#--------------------------------------------------------------
def consultaContinente():
    os.system('cls')
    continente = input("Indique o continente:")

    print("\n\n\t     Países          Continente")
    print("\n\n\t---------------------------------")
    listaPaises = lerFicheiro()
    for linha in listaPaises:
        listaPosicao = linha.split(";")
        if continente == listaPosicao[1].strip('\n'):
            if len(listaPosicao[0]) <=6:
                listaPosicao[0]+= "\t"
            print("\t",listaPosicao[0],"\t\t", listaPosicao[1])
    input()

#---------------------------------------------------------
def consultaNumPaises():
    """
    Imprime o nº de países por continente 
    """
    os.system('cls')
    print("\n\n\t\t---------------------------------")
    print("\t\t    Nº Países      Continente")
    print("\t\t---------------------------------")

    listaPaises = lerFicheiro()
    #listaPaises = listaPaises.strip("\n")
    for continente in listaContinentes:
        numeroPaises = 0
        for linha in listaPaises:
            if linha.split(";")[1].strip("\n") == continente:
                numeroPaises +=1
        print("\t\t\t", numeroPaises, "\t\t", continente)
    input()



# Variáveis globais do programa, que definem o nome da pasta e do ficheiro (path incluida)
ficheiro = ".\\files\\paises.txt"

filePaises = open (ficheiro, "a")
filePaises.close()

opcao = "1"
while opcao != "0":
    os.system("cls")
    print("\n\n\tMENU")
    print("\t1 - Inserir Países")
    print("\t2 - Consulta Ficheiro")
    print("\t3 - Consulta por continente")
    print("\t4 - Consulta nº países")
    print("\t0 - Sair")
    opcao = input("\t\t opção: ")
    if opcao =="1":
        inserePais()
    elif opcao =="2":
        consultaPaises()
    elif opcao == "3":
        consultaContinente()
    elif opcao == "4":
        consultaNumPaises()