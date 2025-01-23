# Biblioteca Tkinter: UI
from tkinter import *
from tkinter import messagebox

fProvas= "files/provas.txt"


def contarProvas(tree, numProvas):
    numProvas.set(len(tree.get_children()))
    


def filtrarAtividades(tree, choice1, choice2, choice3, choice4, numProvas):
    tree.delete(*tree.get_children())

    fileProvas=open(fProvas, "r", encoding="utf-8")
    lista = fileProvas.readlines()
    fileProvas.close()
    cont=0
    for prova in lista:
        if prova == "": continue
        if prova.split(";")[3][:-1] == "5K" and choice1.get():
            tree.insert("", "end", values = (prova.split(";")[0],prova.split(";")[1], prova.split(";")[2], prova.split(";")[3] ))
        if prova.split(";")[3][:-1] == "10K" and choice2.get():
            tree.insert("", "end", values = (prova.split(";")[0],prova.split(";")[1], prova.split(";")[2], prova.split(";")[3] ))
        if prova.split(";")[3][:-1] == "21K" and choice3.get():
            tree.insert("", "end", values = (prova.split(";")[0],prova.split(";")[1], prova.split(";")[2], prova.split(";")[3] ))
        if prova.split(";")[3][:-1] == "Caminhada" and choice4.get():
            tree.insert("", "end", values = (prova.split(";")[0],prova.split(";")[1], prova.split(";")[2], prova.split(";")[3] ))
    contarProvas(tree, numProvas)