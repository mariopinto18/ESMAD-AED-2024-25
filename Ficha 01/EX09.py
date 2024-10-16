
# Calcula o IMC (Índice de Massa Corporal), dado o peso e a altura

peso = float(input("Peso (kg):"))
altura =float(input("\nAltura(m):"))

#Calcula e imprime o índice de massa corporal, IMC
indiceImc = peso/(pow(altura,2))
print(f'\nO seu IMC é: {indiceImc:.2f}')

# categoriza o indivíduo conforme o IMC obtido
if indiceImc < 18.5:
    print("\tBaixo Peso")
elif indiceImc < 25:
    print("\tPeso Normal")
elif indiceImc < 30:
    print("\tExcesso de Peso")
elif indiceImc < 35:
    print("\tObesidade Grau I")
elif indiceImc <40:
    print("\tObesidade Grau II)")
else:
    print("\tObesidade Grade III (morbida)")