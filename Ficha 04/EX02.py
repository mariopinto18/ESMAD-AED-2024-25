import random

def generateNumbers(lim_inf, lim_sup, qt):
    """
    generates qt random values ​​between lim_inf and lim_sup
    returns a list of the generated random values
    """
    chave = []
    i=0
    while i <qt:                          # ciclo que controla a quantidade de nº gerados
        numero = random.randint(lim_inf,lim_sup)    # gera nº aleatorio
        if numero not in chave:                     # se nº gerado NAO EXISTE na lista
            chave.append(numero)                    # acrescenta à lista
            i+=1
    return chave


# Inicio da execução do programa
op = "S"
while op.upper() == "S":
    print("\n Chave do Euromilhões: ", generateNumbers(1,50,5), "\t Estrelas: ", generateNumbers(1,12,2))

    op = input("Deseja gerar nova chave(S/N)?:")
  



