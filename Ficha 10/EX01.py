# Biblioteca Tkinter: UI
import customtkinter
from PIL import Image, ImageTk
import CTkMessagebox
from tkinter import ttk # treeview
import os
import datetime


# path do ficheiro
ficheiro = ".\\files\\presencas.txt"




def lerFicheiro():
    """
    Lista com movimentos existentes em ficheiro
    """
    listaMov = []
    if os.path.exists(ficheiro):   # Ficheiro existe
        fileAcessos = open(ficheiro, "r", encoding="utf-8")
        listaMov = fileAcessos.readlines()
        fileAcessos.close()    
    return listaMov



def refreshPresenças(textMov):
    listaMov= lerFicheiro()
    textMov.insert("0.0", "Número    \tData \tHora \tMovimento\n")
    for linha in listaMov:
        linha = linha.replace(";", "   -   ")
        textMov.insert("end", linha)



def registarFicheiro(entryAluno, cb1, cb2):
    # Obter Nº de aluno
    linha = entryAluno.get()
   # Obter data e hora
    data = datetime.date.today()
    linha+=";" + str(data) 
    # Obter hora
    hora = datetime.datetime.now().time().strftime("%H:%M:%S")
    linha+= ";"+ str(hora)

    # Obter tipo movimento entrada opu Saida
    if cb1.get() == "on":
            linha += ";" + "Entrada\n"
    elif cb2.get() == "on":
         linha += ";" + "Saída\n"

 
    # Guardar em ficheiro de presencas.txt
    fileAcessos = open(ficheiro, "a", encoding="utf-8")
    fileAcessos.write(linha)
    fileAcessos.close()




#-------------------------------------------------------------------------
def gerirPresencas():

# FRAME
    frameGerir = customtkinter.CTkFrame(app, width = 750, height = 500)
    frameGerir.place(x=250, y=0) 
   
    labelAluno = customtkinter.CTkLabel(frameGerir, text ="Número de estudante")
    labelAluno.place(x=25, y=60)

    entryAluno = customtkinter.CTkEntry(frameGerir, width=200)
    entryAluno.place(x=150, y=60)

    labelTipoMov = customtkinter.CTkLabel(frameGerir, text ="Tipo de Movimento")
    labelTipoMov.place(x=25, y=100)

    # CheckButtons
    cb1 = customtkinter.StringVar()
    cb2 = customtkinter.StringVar()

    ck1 = customtkinter.CTkCheckBox(frameGerir, text = "Entrada", variable = cb1, onvalue = "on", offvalue="off")
    ck1.place(x=150, y=100)
    ck2 = customtkinter.CTkCheckBox(frameGerir, text = "Saída", variable = cb2, onvalue = "on", offvalue="off")
    ck2.place(x=150, y=140)

    labelHist = customtkinter.CTkLabel(frameGerir, text ="Histórico de presenças", text_color="red", font=("Helvetica", 15))
    labelHist.place(x=440, y=40)
    
    textMov = customtkinter.CTkTextbox(frameGerir, width=320, height=300, fg_color="gray", text_color="white")
    textMov.place(x=400, y=70)

    # Buttons
    btnregistar = customtkinter.CTkButton(frameGerir, text ="Registar o Movimento \nem Ficheiro", fg_color="black", text_color="cyan",
                        width=250, height=170, command = lambda: registarFicheiro(entryAluno, cb1, cb2))
    btnregistar.place(x=70, y=280)
    
    btnLerFile = customtkinter.CTkButton(frameGerir, text ="Ler Ficheiro de Presenças", fg_color="black", text_color="cyan",
                        width=320, height=70, command = lambda: refreshPresenças(textMov))
    btnLerFile.place(x=400, y=380)
    


#-------------------------------------------------------------------------
def renderConsulta():
    """
    renderiza Frame da opção Consulta de movimentos
    """
  
    # FRAME
    frameCons = customtkinter.CTkFrame(app, width = 750, height = 500)
    frameCons.place(x=250, y=0) 
    #Frame Tipo de Movimento - checkbuttons para entradas / saídas
    lframe1 = customtkinter.CTkFrame(frameCons, width = 220, height=100, fg_color="gray") 
    lframe1.place(x=20, y=15)

    labelTipoMov = customtkinter.CTkLabel(lframe1, text ="Tipo de Movimento", text_color="white")
    labelTipoMov.place(x=15, y=10)

    # CheckButtons
    cb1 = customtkinter.IntVar()
    cb2 = customtkinter.IntVar()
    ck1 = customtkinter.CTkCheckBox(lframe1, text = "Entrada", text_color="white", variable = cb1)
    ck1.place(x=30, y=40)
    ck2 = customtkinter.CTkCheckBox(lframe1, text = "Saída", text_color="white", variable = cb2)
    ck2.place(x=30, y=70)


    # FRAME 2 - entry para indicar nº de utilizador a consultar
    lframe2 = customtkinter.CTkFrame(frameCons, width = 220, height=100, fg_color = "gray")
    lframe2.place(x=250, y=15)
    
    labelNumero = customtkinter.CTkLabel(lframe2, text ="Número", text_color="white")
    labelNumero.place(x=50, y=15)

    ##Entry    
    utilizador = customtkinter.StringVar()
    txtUtilizador = customtkinter.CTkEntry(lframe2, width = 150, textvariable = utilizador)
    txtUtilizador.place(x=25, y=50)

    #  Button consultar dados
    img1 = customtkinter.CTkImage(Image.open(".\\images\\lupa.png"), size=(64, 64))
    btnConsultar = customtkinter.CTkButton(frameCons, width = 220, height= 100, image = img1, text = "", 
                        command = lambda: consultaMovimentos(cb1, cb2, utilizador, tree))
    btnConsultar.place(x=480, y=15)


    # FRAME 3
    frame3 = customtkinter.CTkFrame(frameCons, width = 690, height = 500)
    frame3.place(x=20, y=170)

    # TreeView para consulta de movimentos
    tree = ttk.Treeview(frame3, height = 16, selectmode = "browse", 
                  columns = ("Número", "Data", "Hora", "Movimento"), 
                  show = "headings")
    
    tree.column("Número", width = 160,  anchor="c")
    tree.column("Data", width = 160,     anchor="c")        # c- center
    tree.column("Hora", width = 160,     anchor="c")        # e - direita
    tree.column("Movimento", width = 200, anchor="c")       # w- esquerda
    tree.heading("Número", text = "Número")
    tree.heading("Data", text = "Data")
    tree.heading("Hora", text = "Hora")
    tree.heading("Movimento", text = "Movimento")
    tree.place(x= 70, y=15)

    # Scrollbar Vertical
    verscrlbar = ttk.Scrollbar(frame3, orient ="vertical", command = tree.yview)
    # CallinPlace da Scrollbar
    verscrlbar.place(x=735, y=16, height=330)
    # Adicionar scrollbar à  treeview
    tree.configure(yscrollcommand = verscrlbar.set)
    





def consultaMovimentos(cb1, cb2, utilizador, tree):  
    """
    Consulta movimentos em Treeview, de acordo com filtros selecionados
    """
    tree.delete(*tree.get_children()) 
    mov = ""
    if cb1.get() == True and cb2.get() == True:   # Se está checado entrada e saída (cb1 e cb2)
        mov = "T"
    else:
        if cb1.get() == True:                      # se está apenas checado cb1 (entrada)
            mov = "Entrada\n"
        if cb2.get() == True:                      # se está apenas checado cb2 (saida)
            mov = "Saída\n"
    
    lista = lerFicheiro()
    for linha in lista:
        campos = linha.split(";")
        if mov == "T" or  campos[3] == mov:
            if utilizador.get() == "" or utilizador.get() == campos[0]:
                    tree.insert("", "end", values = (campos[0], campos[1], campos[2], campos[3]))

    # como adionar hedings que permitem, ordenar colunas numa tree 
    columns = ['Número', 'Data', 'Hora', 'Movimento']
    for col in columns:
            tree.heading(col, text=col, command=lambda _col=col:\
                     treeview_sort_column(tree, _col, False))



   


#----------------------------------------------------
# GUI -----------------------------------------------
#----------------------------------------------------
def renderWindow(appWidth, appHeight, appTitle):
    """
    Renderiza a window da app, com as dimensões e título dos argumentos
    """
    app.title(appTitle)
    # Obter as dimensões do meu screen (em pixeis)
    screenWidth = app.winfo_screenwidth()
    screenHeight = app.winfo_screenheight()
    # App centrada no screen, em função das suas dimensões# encontrar o 
    x = (screenWidth/2) - (appWidth/2)
    y= (screenHeight/2) - (appHeight/2)
    app.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
    app.resizable(False, False) 



def confirmarSair():
    """
    messabebox com mensagem de confirmação de saída da aplicação
    """
  # messagebox ask question
    msg = CTkMessagebox.CTkMessagebox(title="Gestão de Presenças", message="Deseja mesmo encerrar a aplicação?",
                        icon="question", option_1="Não", option_2="Sim")
    response = msg.get()
    
    if response=="Sim":
        app.destroy()   





#------INICIO DA APLICAÇÃO

listaMov = lerFicheiro()  ## carrega ficheiro para lista

#-----Arranque da aplicação --------------------------------
#----------------------------------------------------------
app=customtkinter.CTk()   # invoca classe Ctk , cria a "main window"
renderWindow(1000, 500, "Gestão de Presenças")

# PAINEL OPÇÕÊS
# FRAME COM  OPÇÕES
frameMenu = customtkinter.CTkFrame(app,  fg_color = "black", width=250, height=500)
frameMenu.place(x=0, y=0)



imageIco1 = customtkinter.CTkImage(Image.open(".\\images\\icoOp1.png"), size=(64, 64))
btnOpcao1 = customtkinter.CTkButton(frameMenu, text = "Gerir Presenças", image = imageIco1, compound="top", 
                    width = 230, height = 120, font=("Calibri", 14),
                    command=gerirPresencas)
btnOpcao1.place (x=5, y=50)

imageIco2 = customtkinter.CTkImage(Image.open(".\\images\\icoOp2.png"), size=(64, 64))
btnOpcao2 = customtkinter.CTkButton(frameMenu, text = "Consultar Presenças", image = imageIco2, compound="top",
                width = 230, height = 120,  font=("Calibri", 14),
                command= renderConsulta)
btnOpcao2.place (x=5, y=190)


imageIco4 = customtkinter.CTkImage(Image.open(".\\images\\icoOp4.png"), size=(64, 64))
btnOpcao4 = customtkinter.CTkButton(frameMenu, text = "Sair App", image = imageIco4, compound="top",
                width = 230, height = 120,  font=("Calibri", 14), 
                command = confirmarSair)
btnOpcao4.place (x=5, y=330)

imageLabel = customtkinter.CTkImage(Image.open(".\\images\\presencas.png"), size=(750, 500))
labelUI = customtkinter.CTkLabel(app, image = imageLabel, text = "", width = 100, height=100 )
labelUI.place(x= 250, y=0)


















app.mainloop()   # event listening loop by calling the mainloop()
