""""
Dado uma conjunto de n números (n indicado pelo utilizador) inteiros
e positivos, determine o segundo maior valor de entre o conjunto de números
lido
"""

primeiroMaior = 0    # Maior numero 
segundoMaior = 0     # segundo maior numero

n= int(input("Qts numeros dejesa ler? "))
for i in range(n):                  # ler n numeros
    numero = int(input("Número: "))
    if numero > primeiroMaior:      # verificar se é o maio numero
        segundoMaior= primeiroMaior
        primeiroMaior=numero
    elif numero > segundoMaior:     # verificar se é superior ao 2º maior
        segundoMaior=numero

print(f'\n\n\t\tSegundo maior valor da lista de números lidos é: {segundoMaior}' )
