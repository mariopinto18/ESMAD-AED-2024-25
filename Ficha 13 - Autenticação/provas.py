# Biblioteca Tkinter: UI
from tkinter import *
from tkinter import messagebox
from tkinter import ttk          # extensão do tkinter, inclui treeview

fProvas= "files/provas.txt"


def inserirProva(prova, data, local, tipoProva, tview):
    fileProvas=open(fProvas, "a", encoding="utf-8")
    linha = prova + ";" + data + ";" + local + ";" + tipoProva + "\n" 
    fileProvas.write(linha)
    fileProvas.close()
    
    lista = lerProvas()
    refreshListboxProvas(lista, tview)
   


def removerProva(tview):
    #rowId = tview.focus()
    #linha= tview.item(rowId)
    #print(linha)
    
    tview.delete(tview.selection())

    fileProvas=open(fProvas, "w", encoding="utf-8")
    for line in tview.get_children():
           atividade = tview.item(line)["values"][0] + ";" + tview.item(line)["values"][1] + ";"+ tview.item(line)["values"][2] + ";" + tview.item(line)["values"][3]
           fileProvas.write(atividade)         # Guarda em ficheiro
    fileProvas.close()

    lista = lerProvas()
    refreshListboxProvas(lista, tview)


def lerProvas():
    fileProvas=open(fProvas, "r", encoding="utf-8")
    lista = fileProvas.readlines()
    fileProvas.close()
    return lista


def refreshListboxProvas(listaProvas, tview):
    tview.delete(*tview.get_children())
    for item in listaProvas:
        tview.insert("", "end", values = (item.split(";")[0],item.split(";")[1], item.split(";")[2], item.split(";")[3] ))