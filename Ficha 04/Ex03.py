
def positiveList(score):
    """
    receives a list of 10 scores and returns a list with the positive ones
    """
    positiveScore = []                        # Nova lista
    """
    for element in score:
        if element >=10:
            positiveScore.append(element) 
    """
    for i in range (len(score)):
        if score[i] >=10:
            positiveScore.append(score[i])    # adiciona à nova lista
    return positiveScore


# Ler pontuação de 10 participantes e indicar aquelas >=10
score = []
i=1
while i <=10:         # ciclo para ler as 10 pontuações
        try:
            number = int(input("\nPontuação do {0}º participante:" .format(i)))
            if number <0 or number >20:
                raise ValueError()
        except ValueError:
            print("Pontuação inválida. Pf insira valoresno intervalor [0-20]")
        except:
            print("ocorreu um erro inesperado, tente novamente!")
        else:
            score.append(number)
            i+=1

# positiveScore é a lista com pontuações positivas
positiveScore = positiveList(score)
print("\nPontuações positivas: {0} " .format(positiveScore))
