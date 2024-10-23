# Jogo Adivinha o número
# Dado um numero aleatorio, o utilizador deve adivinhá-lo
import random

print("\t\tJOGO Adivinha o Número\n")
numeroGerado = random.randint(1,50)  # gera numero aleatorio entre 1 e 50 - Inclusivé
numTentativas = 1
palpiteUser = int(input("Indique o seu {:n}º palpite: " .format(numTentativas)))

while numeroGerado != palpiteUser and numTentativas <10:     # controla o funcionamento de 1 jogo
    if palpiteUser > numeroGerado:
        print("O número é MENOR \n")
    elif palpiteUser < numeroGerado:
        print("O número é MAIOR \n")
    numTentativas+= 1
    palpiteUser = int(input("Indique o seu {:n}º palpite: " .format(numTentativas)))


# Sai do ciclo while - ou porque acertou ou porque esgotou as 10 tentativas!
if numeroGerado == palpiteUser:
    print("Parabéns! Acertou em {:n} tentativas" .format(numTentativas))
else:
    print("Esgotou as 10 tentativas! :( ")
# - fim do jogo
