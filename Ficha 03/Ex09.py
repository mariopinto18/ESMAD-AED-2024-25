def printCharLine(texto, numCar):
    """
    Recebe um texto e imprime @numCar caracteres por linha
    Args: string, int
    """
    while (len(texto) > numCar):    # enquanto o comprimento do texto > numero de caracteres a imprimir
        print(texto[0:numCar])
        texto=texto[numCar:]
    print(texto)                    # no final do while imprime os caracteres que restam



texto = input("Texto:")
numCar = int(input("\nNº caracteres a imprimir por linha:"))
printCharLine(texto, numCar)

