""" 
Simulador de peso noutros planetas, em função da sua gravidade relativa
Fonte:https://ecoosfera.com/sci-innovacion/cuanto-pesarias-en-otros-planetas/ 
""" 
print("\t\t\t\t\tPlanetas")
print("\t\t\t\t1 - Mercúrio")
print("\t\t\t\t2 - Venus")
print("\t\t\t\t3 - Marte")
print("\t\t\t\t4 - Júpiter")
print("\t\t\t\t5 - Saturno")
print("\t\t\t\t6 - Urano")
print("\t\t\t\t7 - Neptuno")

peso = float(input("\n\nIndique o seu peso (kg):"))
planeta = int(input("\n\nIndique o código do planeta:"))

match planeta:
    case 1: gravidade = 0.37
    case 2: gravidade = 0.90
    case 3: gravidade = 0.37
    case 4: gravidade = 2.53
    case 5: gravidade = 1.06
    case 6: gravidade = 0.91
    case 7: gravidade = 1.14
    case _: 
        print("Código de planeta inválido! :(")
        exit()
            
pesoPlaneta = peso*gravidade / 0.98   # Gravidade na terra
print("\nO seu peso de {:.2f} kg no planeta {:n} seria de {:.2f} Kg" .format(peso, planeta, pesoPlaneta))
