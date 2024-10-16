""" 
Determina a Etapa de Vida, em função da idade indicada pelo utilizador

https://reyabogado.com/brasil/qual-a-idade-de-cada-fase-davida/#:~:
text=Abaixo%20est%C3%A3o%20descritas%20as%209%20fases%
20da%20vida,8%208.%20Velhice%20%2865%20a%2079%20anos%29%3A%20 

"""


idade = int(input("\n\tIndique a sua idade:"))
etapaVida = ""      # inicializa a variável a vazio

if  idade <= 12:
    etapaVida = "Infância"
    if idade <=2:
        etapaVida+= " - Primeira Infância"
    elif idade <= 6:
        etapaVida+= " - Infância Intermédia"
    else:
        etapaVida+= " - Pré-adolescência"
elif idade <= 19:
    etapaVida = "Adolescência"
    if idade <= 14:
        etapaVida+= " - Puberdade"
    else:
        etapaVida+= " - Adolescência tardia"
elif idade  <= 59:
    etapaVida = "Adultez"
    if idade <=39:
        etapaVida+= " - Jovem Adulto"
    else:
        etapaVida+= " - Meia-idade"
else:
    etapaVida = "Terceira Idade"
    if idade <= 74:
        etapaVida+= " - Idosos Jovens"
    else:
        etapaVida+= " - Idosos velhos"
    

print(f'\n\tEtapa de vida: {etapaVida}')