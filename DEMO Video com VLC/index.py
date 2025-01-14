# Biblioteca Tkinter: UI
from tkinter import *
from tkinter import filedialog   # filedialog boxe
from PIL import ImageTk, Image
#from tkVideoPlayer import TkinterVideo
import customtkinter
import webbrowser
import os
os.add_dll_directory(r'C:\Program Files\VLC')

import vlc


# importing time module
import time


fVideos= ".\\files\\playVideos.txt"
selectedVideo = ""



def lerFicheiroText(fileToRead):
    """
    Lê ficheiro de texto passado como argumento da função
    Pode ser ficheiro de playList, playVideos, playYoutube 
    """
    lista = []
    if os.path.exists(fileToRead):   # Ficheiro existe
        file = open(fileToRead, "r", encoding="utf-8")
        lista = file.readlines()
        file.close()    
    return lista


def fileToPlay(fileVideo):
    """
    reter, numa variável global, o ficheiro associado ao button onde cliquei
    """ 
    global selectedVideo
    selectedVideo = fileVideo



def playVideo():
   """
   Play do vídeo: reconstituo a path do caminho para a pasta onde estão os vídeos
   Criar uma instancia com o vídeo e fazer o play
   """
   video = f'.\\files\\videos\\{selectedVideo}' 
   
   global player
   media = Instance.media_new(video)
   player.set_media(media)
   player.play()
   player.audio_set_mute(True)



def stopVideo():
    """
    fazer o stop dop video
    """
    global player
    player.stop()



def pauseVideo():
   """
   fazer o pause dop video
   """
   global player
   player.set_pause(1)


def muteVideo():
   """
   fazer o Mute ou unMute (som) do vídeo
   """
   # making mute status True 
   global player
   value = player.audio_get_mute()
   if value == False:
      player.audio_set_mute(True)
      btnVideoMute.configure(text = "Mute Off") 
   else:
      player.audio_set_mute(False) 
      btnVideoMute.configure(text = "Mute On")





      
def fechaPanelUsers():
   panelUsers.place_forget()    



## ------ Painel para criar conta de utilizador
def registar(funcao, btnSessao):
   if userAutenticado.get() != "":     # SE JÁ EXISTE um user autenticado, a ieia é terminar sessão
      userAutenticado.set("")
      btnSessao.config(text = "Iniciar Sessão")
      return

   panelUsers.place(x=580, y=28)
# Username
   labelUsers = Label(panelUsers, text ="Username:")
   labelUsers.place(x=10, y= 10)
   userName = StringVar()
   txtUser = Entry(panelUsers, width=20, textvariable=userName)
   txtUser.place(x=80, y= 10)
#Password
   labelPass = Label(panelUsers, text ="Password:")
   labelPass.place(x=10, y= 60)
   userPass = StringVar()
   txtPass = Entry(panelUsers, width=20, textvariable = userPass, show = "*")
   txtPass.place(x=80, y= 60)
#Buttons
   if funcao == 1:   # Abre painel para criar conta
      btnUsers = Button(panelUsers, text = "Criar Conta", width = 12, height = 2, 
                 command = lambda: [criaConta(userName.get(), userPass.get()), fechaPanelUsers()])
      btnUsers.place(x=10, y= 110)
      btnCalcel = Button(panelUsers, text = "Cancelar", width = 12, height = 2, command = fechaPanelUsers)
      btnCalcel.place(x=120, y= 110)
   else:         # Abre painel para iniciar sessão
      btnUsers = Button(panelUsers, text = "Iniciar Sessão", width = 12, height = 2, 
                 command = lambda: iniciarSessao(userName.get(), userPass.get())   )
      btnUsers.place(x=10, y= 110)
      btnCalcel = Button(panelUsers, text = "Cancelar", width = 12, height = 2, command = fechaPanelUsers)
      btnCalcel.place(x=120, y= 110)
   

def iniciarSessao(userName, userPass):
   userAutenticado.set(validaConta(userName, userPass))
   if userAutenticado.get() != "":
      btnSessao.config(text = "Terminar Sessão")
      fechaPanelUsers()






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



app=customtkinter.CTk()   # invoca classe Ctk , cria a "main window"
renderWindow(1000, 600, "my VideoList!")



#---- Label com o user autenticado num dado momento
global userAutenticado
userAutenticado = StringVar()
lblUserAutenticado = Label(app, textvariable= userAutenticado)
lblUserAutenticado.place(x=25, y=10)

### Buttons de registar e Iniciar sessão de user 
btnRegister = customtkinter.CTkButton(app, text = "Registar", width = 70, height = 20,  
                              text_color="cyan", fg_color="black",
                              command = lambda: registar(1, btnRegister))
btnRegister.place(x=630, y=3)

#global btnSessao   # este button tanto pode ter o texto Iniciar Sessão como Terminar Sessão
btnSessao = customtkinter.CTkButton(app, text = "Iniciar Sessão", width = 70, height = 20, 
                       text_color="cyan", fg_color="black",
                      command = lambda: registar(2, btnSessao))
btnSessao.place(x=750, y=3)



listaCatalogo = lerFicheiroText(fVideos)  ## carrega ficheiro para lista


# FRAME COM  CATALOGO
frameVideos = customtkinter.CTkScrollableFrame(app,  fg_color = "black", width=230, height=500)
frameVideos.place(x=30, y=70)

# FRAME PARA O PLAY DO VIDEO
framePlay = customtkinter.CTkFrame(app,  fg_color = "black", width=550, height=400)
framePlay.place(x=370, y=70)

#------------------------
Instance = vlc.Instance()                  # Criar uma instância do VLC
player = Instance.media_player_new()       # Criar objeto Media Player 
player.set_hwnd(framePlay.winfo_id())      # Dispor do objeto player dentro de uma frame do Customtkinter (neste exemplo)

#------------------------

# CATALOGO -----------------------------
rowID=1
for linha in listaCatalogo:
    if linha.find(";") == -1: continue
    img, title, mp4File = linha.split(";")
    mp4File=mp4File.replace("\n", "")

    image1 = customtkinter.CTkImage(Image.open(f".\\images\\catalog\\{img}"), size=(128, 128))
            
    e = customtkinter.CTkButton(frameVideos, text=title, image = image1, compound="top",  fg_color="ghost white",
                            width = 160, height = 160, font=("Calibri", 14), text_color="black",
                            command= lambda fileVideo = mp4File: fileToPlay(fileVideo)).grid(column = 1, row = rowID, padx = 20, pady=20) 
            
    rowID+=2


btnVideoPlay = customtkinter.CTkButton(app, text= "Play", width=100, height=40, text_color="cyan", fg_color="black", 
                        command = playVideo).place(x=400, y=510)  

btnVideoPause = customtkinter.CTkButton(app, text= "Pause", width=100, height=40, text_color="cyan", fg_color="black", 
                        command = pauseVideo).place(x=520, y=510)  

btnVideoStop = customtkinter.CTkButton(app, text= "Stop", width=100, height=40, text_color="cyan", fg_color="black", 
                        command = stopVideo).place(x=640, y=510)  

btnVideoMute = customtkinter.CTkButton(app, text= "Mute On", width=100, height=40, text_color="cyan", fg_color="black", 
                        command =  muteVideo)
btnVideoMute.place(x=760, y=510)  


















#------------------------------------------------------------
# Cria Painel para cria conta ou iniciar sessão. O Painel é renderizado APENAS na função registo
global panelUsers
panelUsers = PanedWindow(app, width = 300, height = 200)




app.mainloop()   # event listening loop by calling the mainloop()