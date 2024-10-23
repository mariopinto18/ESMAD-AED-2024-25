# Jogo Adivinha o número
# Dado um numero aleatorio, o utilizador deve adivinhá-lo
import random
import os      # biblioteca oprating system

resposta = "S"
while resposta.upper() != "N":
    os.system("cls")    # função do sistema operativo cls - clear screen

    print("\t\tJOGO Adivinha o Número\n")

    # Inicio do jogo-------
    numeroGerado = random.randint(1,50)  # gera numero aleatorio entre 0 e 50 - Inclusivé
    palpiteUser = int(input("Indique o seu palpite: "))
    numTentativas = 1

    while numeroGerado != palpiteUser and numTentativas <10:     # controla o funcionamento de 1 jogo
        if palpiteUser > numeroGerado:
            print("O número é MENOR \n")
        elif palpiteUser < numeroGerado:
            print("O número é MAIOR \n")
        palpiteUser = int(input("Indique o seu palpite: "))
        numTentativas+= 1

    # Sai do ciclo while - ou porque acertou ou porque esgotou as 10 tentativas!
    if numeroGerado == palpiteUser:
        print("Parabéns! Acertou em {:n} tentativas" .format(numTentativas))
    else:
        print("Esgotou as 10 tentativas! :( ")

    resposta = input("Novo Jogo(S/N)? ")

