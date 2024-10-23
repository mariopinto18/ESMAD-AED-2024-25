"""
dado um número verifica se +e um número perfeito
Numero perfeito : é um nº em que a soma dos seus divisores é igual ao proprio numero
"""

numero = int(input("Indique um número:"))
soma=0
for i in range(numero-1, 0, -1):
    resto = numero % i
    if resto == 0:
        soma+= i

if soma == numero:
    print("O número {0} é um número perfeito" .format(numero))
else:
    print("O número {0} não é um número perfeito" .format(numero))
    