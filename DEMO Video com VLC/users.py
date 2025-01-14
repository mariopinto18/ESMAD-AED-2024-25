# Biblioteca Tkinter: UI
from tkinter import *
from tkinter import filedialog   # filedialog boxe
from PIL import ImageTk, Image
from tkinter import messagebox

fUsers = "utilizadores.txt"

# Funções relacionadas com o User
# Registar, Iniciar Sessão


def validaConta(userName, userPass):
    f=open(fUsers, "r", encoding="utf-8")
    listaUsers = f.readlines()
    f.close()
    for linha in listaUsers:
        fields = linha.split(";")
        if fields[0] == userName and fields[1][:-1] == userPass:
            msg = "Bem-Vindo " + userName
            messagebox.showinfo("Iniciar Sessão", msg)
            return userName
    messagebox.showerror("Iniciar Sessão", "O UserName ou a Password estão incorretos!")
    return ""
    


def criaConta(userName, userPass):
    if userName == "" or userPass == "":
        messagebox.showerror("Criar Conta", "O username e a password não podem ser vazios!")
        return         
    f=open(fUsers, "r", encoding="utf-8")
    listaUsers = f.readlines()
    f.close()
    for linha in listaUsers:
        fields = linha.split(";")
        if fields[0] == userName:
            messagebox.showerror("Criar Conta", "Já existe um utilizador com esse username!")
            return 
    f = open(fUsers, "a")
    linha = userName + ";" + userPass + "\n"
    f.write(linha)
    f.close()
    messagebox.showinfo("Criar Conta", "Conta criada com sucesso!")


