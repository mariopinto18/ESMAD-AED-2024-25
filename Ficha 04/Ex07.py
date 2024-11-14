# Versão que lista a pluviosidade por ordem decrescente, e os respetivos meses

meses = ["Janeiro   ", "Fevereiro", "Março     ", "Abril     ", "Maio     ", "Junho    ", "Julho    ", "Agosto   ", "Setembro   ", "Outubro   ", "Novembro", "Dezembro"]


#Versão 1.0 : Imprime apenas a pluviosidade ordenada por ordem decrescente
def imprime_pluv_v1(pluv):
    pluv.sort()
    pluv.reverse()
    for pluviosidade in pluv:
        print(pluviosidade)


# Versão 2.0: Imprime a pluviosidade por ordem decerscente, e os respetivos meses
def imprime_pluv_v2(pluv):
    pluvOrdenada = pluv.copy()               # cria copia da lista, DUIPLICADO
    pluvOrdenada.sort(reverse=True)          # ordena a lista ordem decerscente
    for i in range(12):
        pos = pluv.index(pluvOrdenada[i])         # obtem posicao na lista original
        print("\t", meses[pos],"\t", pluvOrdenada[i])   # para saber qual o mês que lhe corresponde
        pluv[pos] = -1


pluv = []
for i in range(12):   # ler pluviosidade ao longo dos 12 meses do ano
    valor = int(input("Pluviosidade no mês de {0} \t: " .format(meses[i])))
    pluv.append(valor)
print("\n\n")
imprime_pluv_v2(pluv)
