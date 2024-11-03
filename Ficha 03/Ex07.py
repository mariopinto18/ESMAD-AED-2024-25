
import random

# função geradora de passwords
def generatePassword(userName):
    """
    Gera ukam password baseada no userName
    Args: string
    Returns: string
    """
    if userName.find(" ")!= -1:    # username SEM espaços
        return "username Inválido!"
    
    password = ""         # password é constituída pelas posições PARES, seguidas de random
    for i in range(1, len(userName), 2):       
        password+= userName[i] + str(random.randint(1,9))     
    # no final a password termina com o nº caracteres do userName
    password+= str(len(userName))
    return password


userName = input("Username: ")
passwd= generatePassword(userName)
print("\npassword:{0}" .format(passwd))

