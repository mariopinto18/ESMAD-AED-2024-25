

def searchNumber(lnumbers, numberSearch):
    """
    Receives a list of numbers and a lookup value.
    Returns the position(s) where the search value is
    """
    cont=lnumbers.count(numberSearch)    # diz-me quantas vezes ocorre na lista
    if cont == 0:
         return -1
    #
    positions = ""
    for i in range(len(lnumbers)):
        if lnumbers[i] == numberSearch:
            positions+= " " + str(i+1)
    
    return positions



lnumbers = []
i=1
while i <=10:
    try:
        number = int(input("{0} º Número : " .format(i)))
    except ValueError:
        print("O valor inserido não parece ser um inteiro. Pf tente novamente!")
    except: print("O valor inserido é incorreto. Pf tente novamente!")
    else:
        lnumbers.append(number)     # Acrescenta às listas de numeros  
        i+=1                  

numberSearch = int(input("Valor de pesquisa:"))
positions = searchNumber(lnumbers, numberSearch)
if positions == -1:
    print(" O numero {0} não existe na lista" .format(numberSearch))
else:
    print(" O numero {0}  existe na lista na(s) posição(ões) {1}" .format(numberSearch, positions))

