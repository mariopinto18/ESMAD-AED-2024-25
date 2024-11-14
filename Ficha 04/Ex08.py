

def lista_sem_duplicados(lnumbers):
    """
    Receive a list of numbers and return a list without duplicates
    """
    newList = []
    lnumbers.sort()
    for i in range (0, len(lnumbers)):
        if newList.count(lnumbers[i]) ==0:           # Se não existe na newList
            newList.append(lnumbers[i])
    return newList





lnumbers=[]
n = int(input("Quantos números desejar ler?"))
for i in range (n):
    number = int(input("numero:"))
    lnumbers.append(number)

newList = lista_sem_duplicados(lnumbers)
print(newList)
