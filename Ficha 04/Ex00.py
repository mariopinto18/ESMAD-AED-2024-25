
import random
def generateNumbers(limInf, limSup, qts):
    """
    receives limInf, limSup, and how many numbers we must generate, and returns a list with the generated numbers
    """
    numbers = []
    while len(numbers) < qts:
        number = random.randint(limInf, limSup)
        if number not in numbers:     # SE NAO FOR REPETIDO
            numbers.append(number)
    numbers.sort()
    return numbers

opcao ="S"
while opcao.upper() == "S":
    print("\nChave do Euromilhões:", generateNumbers(1,50,5),   "  Estrelas:" , generateNumbers(1,12,2))
    opcao = input("Deseja Gerar uma nova chave(S/N)? ")






