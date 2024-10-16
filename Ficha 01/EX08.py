"""
Simulador de Peso ideal, considerando o sexo e a altura
Peso ideal = (h-100) - (h-150)/k
k -2 => feminino, k=4 => masculino
"""

sexo = input("Indique o sexo (M/F): ")
if sexo.lower() != "m" and sexo.lower() != "f":
    print("Não inseriu dados corretos")
    exit()
altura = int(input("Indique a altura (cm): "))

if sexo.lower() == "m":           # upper - converte para maiusculas
    k = 4                         # lower - converte para minusculas
else: 
    k = 2

pesoIdeal = (altura - 100) - (altura - 150) / k
print("O Peso Ideal é {:.2f} Kg" .format(pesoIdeal))
