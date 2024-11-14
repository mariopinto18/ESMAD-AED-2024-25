import os

#variáveis globais
compFila = 20
senha=1


def tirarTicket(tickets):
    """
    receives tickets list and generates a new ticket
    """
    global compFila
    if len(tickets) == compFila:   # se a ultima posição da fila está ocupada
        print("\n\n\t\tNão é possível retirar mais senhas de momento")
        input()
        return tickets   
    global senha
    tickets.append(senha)
    print("\n\n\t\tSaiu ticket nº {0}" .format(senha))
    input()
    senha+=1                        # próxima senha a sair
    return tickets


def atendimento(tickets):
    """
    receives tickets list and implements ticket fulfillment
    """
    if len(tickets) == 0:
        print("\n\n\t\tNão há senhas à espera de atendimento")
        input()
        return
    # atende senha que está na posição 0 da lista (mais à frente)     
    print("\n\n\t\tAtendimento Senha nº {}" .format(tickets[0]))
    input()
    #del tickets[0]
    tickets.pop(0)
    return tickets


def atendimentoV2(tickets):
    """
    receives tickets list and implements ticket fulfillment
    """
    if len(tickets) == 0:
        print("\n\n\t\tNão há senhas à espera de atendimento")
        input()
        return
    # atende senha que está na posição 0 da lista (mais à frente)     
    print("\n\n\t\tAtendimento Senha nº {}" .format(tickets[0]))
    input()
    i=1
    global compFila
    while i != 0 and i<compFila:      # para chegar todas as senhas 1 posição à frente
        tickets[i-1] = tickets[i]
        i+=1
    tickets[compFila-1] = 0
    return tickets


def estado(tickets):
    print("\n\n\t\tSenhas por atender {0} " .format(len(tickets)))  
    print("\n\n\t\tSenhas livres      {0} " .format(compFila - len(tickets)))
    print("\n\t\t", tickets)
    input()


tickets= []

op="1"
while op != '0':
    os.system('cls')                # clear screen
    print("\n\t\t\tMENU\n")
    print("\t\t1- Tirar Ticket")
    print("\t\t2- Atendimento")
    print("\t\t3 - Estado da fila de espera")
    print("\t\t0 - Sair")
    op = input("\t\t    Opção: ")
    if op == '1':
        tickets = tirarTicket(tickets)
    if op == '2':
        tickets = atendimento(tickets)
    if op == '3':
        estado(tickets)
