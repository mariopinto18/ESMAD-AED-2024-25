import os
import random

lPaises = []




def lerFicheiro():
    filepaises = open(ficheiro, "r", encoding="utf-8")
    for pais in filepaises:
        lPaises.append(pais[:-1])
    filepaises.close() 
   


def sortearPais():
    pos = random.randint(0, len(lPaises)-1)
    return lPaises[pos]


def imprimePais(paisAdivinhar, numCaracteres):
   i= numCaracteres
   texto = ""
   texto = paisAdivinhar[0:numCaracteres]
   while i < len(paisAdivinhar):
        texto +="_ "
        i+=1
   print("\n\t\t\t", texto)



def jogar(paisAdivinhar):
    tentativas = 0
    palpite = ""
    numCaracteres=1
    while tentativas <3 and palpite.upper() != paisAdivinhar.upper():
        imprimePais(paisAdivinhar, numCaracteres)
        palpite = input("\n\n\t\tQual o país? ")
        numCaracteres+=1
        tentativas+=1
    if palpite.upper() != paisAdivinhar.upper():
        print("\n\n\t\tGamne Over! :( :( :(")
    else:
        print("\n\n\t\tParabéns, acertou!!! :-)")


#-----------------------------------------
ficheiro = ".\\ficheiros\\paises.txt"
pasta = "ficheiros"
if not os.path.isfile(ficheiro):
    print("O ficheiro de países não existe!")
else:
    print("\n\t\t\tJOGO ADIVINHA O PAÍS")
    print()
    lerFicheiro()
    paisAdivinhar= sortearPais()
    #print(paisAdivinhar)
    jogar(paisAdivinhar)
    