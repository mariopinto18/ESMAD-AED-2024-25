""" 
determina o fatorial de um número
"""

numero = int(input("Indique um número: "))

if numero <0:
    print("Indiqe, p.f., um número inteiro >=0")
else:
    # Temos a certeza de ter um numero >=0
    fatorial=1                          # inicializa fatorial a 1
    for i in range(numero, 1, -1):     # repete do numero lido até 1 (decrescente)
        fatorial*=i

    print("Fatorial de {:n} é {:n}" .format(numero, fatorial))

