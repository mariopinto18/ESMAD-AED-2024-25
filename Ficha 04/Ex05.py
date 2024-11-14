
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]


def maiorFaturacao(lFaturacao):
    """ 
    """
    maior = max(lFaturacao)         # maior valor
    pos= lFaturacao.index(maior)    # posição do maior valor na lista
    return(meses[pos])              
    
def menorFaturacao(lFaturacao):
    """ 
    """
    menor = min(lFaturacao)         # menor valor
    pos= lFaturacao.index(menor)    # posição do menor valor na lista
    return(meses[pos])  

def mediaFaturacao(lFaturacao):
    """
    """
    media = sum(lFaturacao) / len(lFaturacao)
    return media


lFaturacao = []
for i in range(12):
    faturacao = int(input("Indique a faturação do mês de {:s}:" .format(meses[i]) ))
    lFaturacao.append(faturacao)

print("\nMês de maior faturação é ", maiorFaturacao(lFaturacao))
print("\nMês de menor faturação é ", menorFaturacao(lFaturacao))
print("\nMédia de faturação é  {:.2f}" .format(mediaFaturacao(lFaturacao)) )
