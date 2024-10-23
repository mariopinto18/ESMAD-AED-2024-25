# Converte numero para binário

numero = int(input("Número: "))
#print(bin(numero))
result = ""
while numero/2 >=1:             # enquanto divisor for pelo menos 2
    resto = int(numero % 2)     # resto da divisão por 2
    result = str(resto) + " " + result  # concatenar o resto à ESQUERDA do resultado
    numero = int(numero/2)      # calcular próximo quociente da divisão

result =  str(numero) + " " + result
print(result)

