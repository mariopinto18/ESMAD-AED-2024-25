# Biblioteca Tkinter: UI
#from tkinter import *
import customtkinter
import CTkMessagebox
from tkinter import ttk          # extensão do tkinter, inclui treeview
from tkinter import filedialog   # filedialog boxes
from PIL import ImageTk,Image    # Imagens .jpg ou .png
#from tkinter import messagebox   #  messagebox
from tkinter import ttk
from users import *
from provas import *
from atividades import *



def containerGerirProvas():
    panelProvas = PanedWindow(window, width = 750, height= 450)
    panelProvas.place(x=250, y= 50)

    lblProva = Label(panelProvas, text = "Prova")
    lblProva.place(x=30, y=70)

    prova = StringVar()
    entryProva = Entry(panelProvas, width=25, textvariable=prova)
    entryProva.place(x=80, y= 70) 

    lblData = Label(panelProvas, text = "Data")
    lblData.place(x=30, y=120)

    data = StringVar()
    entryData = Entry(panelProvas, width=25, textvariable=data)
    entryData.place(x=80, y= 120) 

    lblLocal = Label(panelProvas, text = "Local")
    lblLocal.place(x=30, y=170)

    local=StringVar()
    entryLocal = Entry(panelProvas, width=25, textvariable=local)
    entryLocal.place(x=80, y= 170) 


    lblLocal = Label(panelProvas, text = "Tipo")
    lblLocal.place(x=30, y=220)

    tipoprova = StringVar()
    tipoprova.set("Caminhada")
    rd1 = Radiobutton(panelProvas, text = "Caminhada", value = "Caminhada", variable= tipoprova)
    rd2 = Radiobutton(panelProvas, text = "5K", value = "5K",               variable= tipoprova)
    rd3 = Radiobutton(panelProvas, text = "10K", value = "10K",             variable= tipoprova)
    rd4 = Radiobutton(panelProvas, text = "21K", value = "21K",             variable= tipoprova)
    rd1.place(x= 80, y= 225)
    rd2.place(x= 80, y= 250)
    rd3.place(x= 80, y= 280)
    rd4.place(x= 80, y= 310)

    #lstprovas = Listbox(panelProvas, width = 50, height=12)
    #lstprovas.place(x= 400, y=70)
    
    tview = ttk.Treeview(panelProvas, height=10,  selectmode= "browse", 
            columns = ("Prova", "Data", "Local", "Tipo"), show = "headings")
    
    tview.column("Prova", width = 100,   anchor="c")
    tview.column("Data", width = 100,  anchor="c")          # c- center, e - direita, w- esquerda
    tview.column("Local", width = 100,   anchor="c")
    tview.column("Tipo", width = 140,   anchor="c")
    tview.heading("Prova", text = "Prova")
    tview.heading("Data", text = "Data")
    tview.heading("Local", text = "Local")
    tview.heading("Tipo", text = "Tipo")
    tview.place(x=280, y=70)

   

    listaProvas= lerProvas()
    refreshListboxProvas(listaProvas, tview)

    global image1, image2
    image1 = PhotoImage(file = "imagens\\adicionar.png" )
    btnInserir = Button(panelProvas, image = image1, width=200, height=48, text = "Inserir Prova", compound=LEFT,
                command= lambda: inserirProva(prova.get(), data.get(), local.get(), tipoprova.get(), tview))
    btnInserir.place(x=280, y= 320)
    
    image2 = PhotoImage(file = "imagens\\remover.png" )
    btnRemover = Button(panelProvas, image = image2, width=200, height=48,  text = "Remover Prova", compound=LEFT,
                command= lambda: removerProva(tview))
    btnRemover.place(x=510, y= 320)




def containerConsultarProvas():
    """
    Painel de consulta de provas com filtros e ordenação
    """
    panelCon = PanedWindow(window, width = 750, height= 450)
    panelCon.place(x=250, y= 50)
    choice1 = IntVar()
    choice1.set(1) 
    choice2 = IntVar()
    choice2.set(0) 
    choice3 = IntVar()
    choice3.set(0) 
    choice4 = IntVar()
    choice4.set(0) 

    ck1 = Checkbutton(panelCon, text = " 5K", variable = choice1)
    ck2 = Checkbutton(panelCon, text = "10K ", variable = choice2)
    ck3 = Checkbutton(panelCon, text = "21K", variable = choice3)
    ck4 = Checkbutton(panelCon, text = "Caminhada ", variable = choice4)
    ck1.place(x=50, y=30)
    ck2.place(x=150, y=30)
    ck3.place(x=250, y=30)
    ck4.place(x=350, y=30)

    global imagePesq, imageAsc, imageDesc
    imagePesq = PhotoImage(file = "imagens\\pesquisar.png")
    imageAsc  = PhotoImage(file = "imagens\\asc.png")
    imageDesc = PhotoImage(file = "imagens\\desc.png")

    btnPesquisar = Button(panelCon, width=48, height=48, image = imagePesq, 
            command = lambda: filtrarAtividades(tree, choice1, choice2, choice3, choice4, numProvas))
    btnOrdenarAsc   = Button(panelCon, width=48, height=48, image = imageAsc)
    btnOrdenarDesc   = Button(panelCon, width=48, height=48, image = imageDesc)
    btnPesquisar.place(x=450, y= 20)
    btnOrdenarAsc.place(x=550, y= 20)
    btnOrdenarDesc.place(x=650, y= 20)


    tree = ttk.Treeview(panelCon, columns = ("Prova", "Data", "Local", "Distancia"), show = "headings", height = 12, selectmode = "browse")
    tree.column("Prova", width = 220, anchor = "w")
    tree.column("Data", width = 100, anchor = "c")
    tree.column("Local", width = 220, anchor = "c")
    tree.column("Distancia", width = 220, anchor = "c")

    tree.heading("Prova", text = "Prova")
    tree.heading("Data", text = "Data")
    tree.heading("Local", text = "Local")
    tree.heading("Distancia", text = "Distancia")
    tree.place(x=20, y=90)
      
    lbNumProvas = Label(panelCon, text = "Nº de provas", font = ("Helvetica", "10"))
    lbNumProvas.place(x=50, y=400)

    numProvas = StringVar()
    txt_num_provas = Entry(panelCon, width=10, textvariable = numProvas)
    txt_num_provas.place(x=150, y=400)







def panelAutenticarUser():
   """
   Painel de autenticação
   """

   if userAutenticado.get() != "":     # SE JÁ EXISTE um user autenticado, a ieia é terminar sessão
        userAutenticado.set("")
        btnIniciarSessão.config(text = "Iniciar Sessão")
        return
   panelUsers = PanedWindow(window, width = 550, height = 300, relief = "sunken")
   panelUsers.place(x=450, y=100)    # 450, 50
 
# Imagem
   containerImage = Canvas(panelUsers, height = 128, width=128)
   containerImage.place(x=50, y=70) 
   global img
   img = PhotoImage(file = ".\imagens\\loginCanvas.png")
   containerImage.create_image(64, 64, image = img)
  # Username
   labelUsers = Label(panelUsers, text ="Username:")
   labelUsers.place(x=200, y= 100)
   userName = StringVar()
   txtUser = Entry(panelUsers, width=20, textvariable=userName)
   txtUser.place(x=280, y= 100)
#Password
   labelPass = Label(panelUsers, text ="Password:")
   labelPass.place(x=200, y= 150)
   userPass = StringVar()
   txtPass = Entry(panelUsers, width=20, textvariable = userPass, show = "*")
   txtPass.place(x=280, y= 150)

   btnValidar= Button(panelUsers, text = "Validar Conta", width=25, height=3,
                      command = lambda: autenticarUser(userName.get(), userPass.get(), panelUsers))
   btnValidar.place(x=260, y= 200) 
   




def autenticarUser(userName, userPass, panelUsers):
   global userAutenticado
   userAutenticado.set(validaConta(userName, userPass))
   if userAutenticado.get() != "":
      btnIniciarSessão.config(text = "Terminar Sessão")
      panelUsers.place_forget()
      containerHome()



def panelCriarConta():
   panelUsers = PanedWindow(window, width = 550, height = 300, relief = "sunken")
   panelUsers.place(x=450, y=100)    # 450, 50
   # Imagem
   containerImage = Canvas(panelUsers, height = 128, width=128)
   containerImage.place(x=50, y=70) 
   global img
   img = PhotoImage(file = ".\imagens\\loginCanvas.png")
   containerImage.create_image(64, 64, image = img)
# Username
   labelUsers = Label(panelUsers, text ="Username:")
   labelUsers.place(x=200, y= 50)
   userName = StringVar()
   txtUser = Entry(panelUsers, width=20, textvariable=userName)
   txtUser.place(x=280, y= 50)
#Password
   labelPass = Label(panelUsers, text ="Password:")
   labelPass.place(x=200, y= 100)
   userPass = StringVar()
   txtPass = Entry(panelUsers, width=20, textvariable = userPass, show = "*")
   txtPass.place(x=280, y= 100)
#Password
   labelPass = Label(panelUsers, text ="Password:")
   labelPass.place(x=200, y= 150)
   userPassConfirm = StringVar()
   txtPass = Entry(panelUsers, width=20, textvariable = userPassConfirm, show = "*")
   txtPass.place(x=280, y= 150)

   btnValidar= Button(panelUsers, text = "Criar Conta", width=25, height=3,
                      command = lambda: [criaConta(userName.get(), userPass.get(), userPassConfirm.get(), panelUsers), containerHome()])
                     
   btnValidar.place(x=260, y= 200) 



def containerHome():
   #-- Painel com opções de menu
   panel2 = PanedWindow(window, width=750, height=450)
   panel2.place(x=250, y=50)
   #------------- Imagem de entrada da App
   ctnCanvas = Canvas(panel2, width = 750, height= 450)
   ctnCanvas.place(x=0, y= 0)
   global img
   img = PhotoImage(file = ".\imagens\\running.png")
   ctnCanvas.create_image(375, 225, image = img)



# ---------------Main-------------------------------------------
#----------------------------------------------------------------
window = Tk()
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
appWidth = 1000                             # tamanho (pixeis) da window a criar 900 / 500
appHeight = 500 
x = (screenWidth/2) - (appWidth/2)        # posição do canto superior esquerdo da window
y = (screenHeight/2) - (appHeight/2)
window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))
window.title('my Running App')

#-- Painel com opções de menu
panel1 = PanedWindow(window, bg = "gray", width=250, height=500)
panel1.place(x=0, y=0)

imageHome = PhotoImage(file = "imagens\\icoHome.png" )
btnHome = Button(panel1, text = "Início \nHome", image = imageHome, compound=LEFT, relief = "sunken", 
                    width = 230, height = 68, font="calibri, 11",
                    command=containerHome)
btnHome.place (x=5, y=50)

imageIco1 = PhotoImage(file = "imagens\\icoOp1.png" )
btnOpcao1 = Button(panel1, text = "Gerir \nProvas", image = imageIco1, compound=LEFT, relief = "sunken", 
                    width = 230, height = 68, font="calibri, 11",
                    command=containerGerirProvas)
btnOpcao1.place (x=5, y=130)

imageIco2 = PhotoImage(file = "imagens\\icoOp2.png" )
btnOpcao2 = Button(panel1, text = "Consultar \nProvas", relief = "sunken", image = imageIco2, compound=LEFT,
                width = 230, height = 68,  font="calibri, 11",
                command= containerConsultarProvas)
btnOpcao2.place (x=5, y=210)

imageIco3 = PhotoImage(file = "imagens\\icoOp3.png" )
btnOpcao3 = Button(panel1, text = "Dashboard\nÁrea Pessoal", relief = "sunken", image = imageIco3, compound=LEFT,
                width = 230, height = 68,  font="calibri, 11", state="disabled")
btnOpcao3.place (x=5, y=290)

imageIco4 = PhotoImage(file = "imagens\\icoOp4.png" )
btnOpcao4 = Button(panel1, text = "Sair App", relief = "sunken", image = imageIco4, compound=LEFT,
                width = 230, height = 68,  font="calibri, 11", 
                command = window.destroy)
btnOpcao4.place (x=5, y=370)




# ------------- HEADER
global userAutenticado
userAutenticado = StringVar()
userAutenticado.set("")
labelHeader = Label(window, textvariable= userAutenticado, fg = "blue", font="calibri, 11")
labelHeader.place(x= 310, y= 10)

imageLogin = PhotoImage(file = "imagens\\icoLogin.png" )
btnIniciarSessão = Button (window, image = imageLogin, relief = "flat",  compound=TOP,
                     width = 78, height=38, text = "Iniciar Sessão", command = panelAutenticarUser)
btnIniciarSessão.place(x=790, y=5)

imageConta = PhotoImage(file = "imagens\\icoConta.png" )
btnCriarConta = Button (window, image = imageConta, width = 64, height=38, relief="flat", text = "Criar Conta",
                  compound = TOP, command=panelCriarConta)

btnCriarConta.place(x=890, y=5)

containerHome()






window.mainloop()   # event listening loop by calling the mainloop()