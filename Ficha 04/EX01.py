
# recebe uma lista de numeros e devolve quantos são superiores à media
def aboveAverage(listNumbers):
    """
    receives a list of numbers and returns how many numbers are above average
    """
    media = sum(listNumbers) / len(listNumbers)   # calcula a media
    cont = 0
    for i in range (len(listNumbers)):
        if listNumbers[i] > media:
            cont+=1
    return cont


# Ler 10 numeros e indicar quts estão acima da média
listNumbers = []
i=1
while i<=10:   # ler 10 numeros e adicinar à lista
        numero = int(input("{0}º Número:" .format(i)))
        listNumbers.append(numero)
        i+=1
print("\n", listNumbers)
print("\nExistem {0} numeros acima da média" .format(aboveAverage(listNumbers)))


