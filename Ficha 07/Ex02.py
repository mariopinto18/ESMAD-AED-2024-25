import os



def lerFicheiro():
    fileTemp = open(ficheiro, "r", encoding="utf-8")
    listaTemp = fileTemp.readlines()
    fileTemp.close()
    return listaTemp


def consulta_data():
    """
    Esta função conulta os dads do ficheiro temperatura.txt
    em função de uma data 
    """
   
    listaTemp= []
    data = input("\n\n\t\tData da consulta: ")
   #--- cabeçalho ----
    print("\t\t\t Data            Hora        Temperatura")
    print("\t\t\t-------------------------------------------")
    
    cont=0
    listaTemp = lerFicheiro()       # ler fx. temperatura-txt
    for linha in listaTemp:         ## ler lista com dados do fx
        campos = linha.split(";")
        if data == campos[0]:        # se data de input = data no ficheiro
            print("\t\t\t", campos[0],"\t", campos[1], "\t", campos[2].strip('\n')  )
            cont+=1
    if cont == 0:
        print("Não existem dados para a data indicada!")
    input()


def consulta_estatistica():
    """
    Consulta a média, o maior e o menso valor de temperatura
    """
    lTemps= []  # Lista vai conter APENAS com temperaturas do ficheiro
    listaTemp = lerFicheiro()       # ler fx. temperatura-txt
    for linha in listaTemp:         ## ler lista com dados do fx
        campos = linha.split(";")
        lTemps.append(int(campos[2].strip('\n')))
    
    print("\n\n\n\t\tO Maior valor de temperatura registada foi de:" , max(lTemps))
    print("\n\n\n\t\tO Menor valor de temperatura registada foi de:" , min(lTemps))
    print("\n\n\n\t\tO valor médio de temperatura registada foi de:" , sum(lTemps)/ len(lTemps))
    input()





# ----- Inicio do programa -------
ficheiro = "temperatura.txt"
opcao = '1'
while opcao != '0':
    os.system("cls")
    print("\n\nMENU")
    print("1 - Consulta por data")
    print("2 - Consulta Estatistica")
    print("0 - Sair")
    opcao = input("\t opção: ")
    match opcao:
        case '1':
            consulta_data()
        case '2':
            consulta_estatistica()

