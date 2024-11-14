# Ler nomes e pontuação de 10 participantes e indicar aquelas >=10
import os

def positiveList(names, score):
    """
    receives a list of 10 scores and returns a list with the positive ones
    """
    pscore = []                       # Nova lista
    pnames = []
    for i in range (len(score)):
        if score[i] >=10:
            pscore.append(score[i])    # adiciona à nova lista
            pnames.append(names[i])        # adiciona nomes à nova lista
    return pnames, pscore


names = []
score = []
i=1
while i <=10:                            # ciclo para ler as 10 pontuações
    try:
        name = input("\nNome do participante {0}  : " .format(i))
        number = int(input("Pontuação participante {0}: " .format(i)))
        if number <0 or number >20:         # cria exceção para valores inferiores a 0 ou >20
            raise ValueError()
    except ValueError:
        print("Pontuação fora dos limites válidos. Pf tente novamente!")
    except:
        print("Pontuação inválida. Pf tente novamente!")
    else:
        names.append(name)                # Acrescenta às listas
        score.append(number)
        i+=1

pnames, pscore = positiveList(names, score)

os.system("cls")
print("Participantes com pontuações positivas \n")
print("Nomes     :", pnames)
print("Pontuações:", pscore)
