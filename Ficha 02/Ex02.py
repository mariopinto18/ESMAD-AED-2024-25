"""
Este programa lê 2 números e calcula a soma
de todos os pares entre eles 
"""

limiteInf =int(input("Indique o limite Inferior:"))
limiteSup =int(input("Indique o limite  superior:"))

somaNumeros=0
for i in range(limiteInf, limiteSup+1):
    if i % 2 ==0:                 # se número é par
        somaNumeros+= i           # soma-o
        
print(f"A soma de todos os pares entre {limiteInf} e {limiteSup} é {somaNumeros}")