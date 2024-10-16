"""
Lê um numero e determina se é par ou impar
"""
numero = int(input("Indique um número inteiro:"))
if numero % 2  == 0:
    print(f'\nO número  {numero} é par')
else:
    print(f'\nO número  {numero} é ímpar')