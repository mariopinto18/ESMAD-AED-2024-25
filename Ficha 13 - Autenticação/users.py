# Biblioteca Tkinter: UI
from tkinter import *
from tkinter import messagebox



# Funções relacionadas com o User
# Registar, Iniciar Sessão
fUsers= "files/utilizadores.txt"

def validaConta(userName, userPass):
    """
    Validar cautenticação com uma conta
    """
    fileUsers=open(fUsers, "r", encoding="utf-8")
    listaUsers = fileUsers.readlines()
    fileUsers.close()
    for linha in listaUsers:
        if linha.split(";")[0] == userName and linha.split(";")[1][:-1] == userPass:
            msg = "Bem-Vindo " + userName
            messagebox.showinfo("Iniciar Sessão", msg)
            return msg
    messagebox.showerror("Iniciar Sessão", "O UserName ou a Password estão incorretos!")
    return ""



 


def criaConta(userName, userPass, userPassConfirm, panelUsers):
    """
    Criar uma nova conta
    """
    if userPass != userPassConfirm:
        messagebox.showerror("Criar Conta", "A password difere do inserido na sua confirmação!")
        return  
    if userName == "" or userPass == "":
        messagebox.showerror("Criar Conta", "O username e a password não podem ser vazios!")
        return         
    fileUsers=open(fUsers, "r", encoding="utf-8")
    listaUsers = fileUsers.readlines()
    fileUsers.close()
    for linha in listaUsers:
        fields = linha.split(";")
        if fields[0] == userName:
            messagebox.showerror("Criar Conta", "Já existe um utilizador com esse username!")
            return 
    fileUsers = open(fUsers, "a")
    linha = userName + ";" + userPass + "\n"
    fileUsers.write(linha)
    fileUsers.close()
    messagebox.showinfo("Criar Conta", "Conta criada com sucesso!")
    #panelUsers.place_forget()
    panelUsers.destroy()
    

