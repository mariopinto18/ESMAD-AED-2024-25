"""
Imprime os primeiros n termos da 
sequência de Fibanacci
"""
nTermos = int(input("\n\n\n\t\t\t Nº de termos a imprimir:"))

seqTermos= ""
# Tratamos os 3 primeiros termos
if nTermos >= 1:        # trata 1º termo da sequencia
    seqTermos = "0"
if nTermos >= 2:        # trata 2º termo da sequencia
    seqTermos+= ", 1"
penultimoTermo = 0
ultimoTermo = 1

# Tratamos os termos seguintes - do 3º em diante
for i in range(3, nTermos+1):   # para todos a partir do 3º termo
    novoTermo = penultimoTermo + ultimoTermo         # cada termo resulta da soma dos 2 anteriores
    seqTermos+= ", " + str(novoTermo)   # vai contactar os termos numa variavel de texto
                                         # para facilitar a impressão do resultado
    penultimoTermo = ultimoTermo
    ultimoTermo = novoTermo

print(f'\n\n\t\t\t Primeiros {nTermos} termos da sequência de Fibonacci: {seqTermos}')


