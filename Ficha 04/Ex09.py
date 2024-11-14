import math

dias = ["Domingo", "Segunda", "Terça  ", "Quarta ", "Quinta ", "Sexta  ", "Sábado "]


def lista_visiantes(visitantes):
    visitantes_ord = visitantes.copy()  # cria copia da lista
    visitantes_ord.sort(reverse=True)         # ordena a lista
    for i in range(7):
        pos = visitantes.index(visitantes_ord[i])   # obtem posicao na lista original
        print(dias[pos],"\t", visitantes_ord[i])    # para saber qual o mês que lhe corresponde
        visitantes[pos] = -1
    print("Nº médio de visitantes: {:.2f}" .format(sum(visitantes_ord) / len(visitantes_ord)))


# devolve o dia mais proximo do valor médio de visitas
def proximo_media(visitantes):
    media = sum(visitantes) / len(visitantes)
    diferenca = math.inf
    for i in range(0,7):
        if abs(visitantes[i] - media) < diferenca:
            pos = i
            diferenca = abs(visitantes[i] - media) 
    return dias[pos]
        
    


visitantes=[]
for i in range (7):
    num = int(input("Nº visitantes na/no {0} \t: " .format(dias[i])))
    visitantes.append(num)
dia = proximo_media(visitantes)
lista_visiantes(visitantes)
print("Dia mais próximo do valor médio:", dia)

input()

