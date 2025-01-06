# Biblioteca Tkinter: UI
import customtkinter
from PIL import Image, ImageTk
import CTkMessagebox
from tkinter import ttk                 # treeview
import os
import webbrowser                        # https://docs.python.org/3/library/webbrowser.html 
from pygame import mixer                 # https://www.pygame.org/docs/ref/music.html 
from tkVideoPlayer import TkinterVideo   #https://pypi.org/project/tkvideoplayer/ 

                                        # cores: https://www.plus2net.com/python/tkinter-colors.php 
import TextFiles


# path dos ficheiro
fYoutube = ".\\files\\playYoutube.txt"
fSongs = ".\\files\\playList.txt"
fVideos= ".\\files\\playVideos.txt"
selectedSong= ""




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




def confirmarSair(event):
    # messagebox ask question
    msg = CTkMessagebox.CTkMessagebox(app, title="Sair da aplicação", message="Deseja encerrar a aplicação?", bg_color="black", text_color="red",
                     title_color="red", icon="question", option_1="Não", option_2="Sim")
    response = msg.get()
    
    if response=="Sim":
        app.destroy()  
    # Definir o tabulador ativo / visível num dado momento
    tabview.set(" Home ")





# WEBBROWSER ------------------------------
#-----------------------------------------
def playWebBrowserVideo(url):
    """
    Abre o browser definido por defeito com um url
    """
    webbrowser.open(url, new = 0, autoraise=True)          #the window is raised if possible
    
    """ 
    If new is 0, the url is opened in the same browser window if possible. 
    If new is 1, a new browser window is opened if possible. 
    If new is 2, a new browser page (“tab”) is opened if possible. 
"""


# SOUND --------------- reproduzir ficheiros MP3, p.e.
# MIXER SOUND -------------------------------
def playSound(fileSong):
    """
    reter, numa variável global, o ficheiro associado ao button onde cliquei
    """ 
    global selectedSong
    selectedSong = fileSong


def mixerSound():
    """
    fazer o load do ficheiro e o play 
    """
    song = f'.\\files\\songs\\{selectedSong}'
    mixer.music.load(song)  #Loading Music File
    mixer.music.play()      #Playing Music with Pygame


def mixerPause():
    mixer.music.pause()


def mixerStop():
    mixer.music.stop()




#  tvVideoPlayer - reproduzir Video, p.e. mp4
#----------------------------------------------
# reprodução de vídeo 
def playVideo():
  videoPlayer.bind("<<Loaded>>", lambda e: e.widget.config(width=500, height=400))

  video = f'.\\files\\videos\\{selectedSong}' 
  videoPlayer.load(video)
  videoPlayer.set_size([400,300])  # width, height
  videoPlayer.set_scaled=True
  videoPlayer.play() # play the video
  


def pauseVideo():
   if videoPlayer.is_paused():
       videoPlayer.play()
   else:
       videoPlayer.pause()


def stopVideo():
    videoPlayer.stop()



def seekVideo(value):
    """ used to seek a specific timeframe """
    videoPlayer.seek(int(value))




#-----Arranque da aplicação --------------------------------
# INTERFACE GRAFICA DA APLICAÇÃO 
app=customtkinter.CTk()   # invoca classe Ctk , cria a "main window"
renderWindow(1000, 600, "my Catalog!")
#------------------------------------------------------------
# TABVIEW
# tab métodos: 
# insert(index, name), add(name) rename(name1, name2), delete(name), index(name), set(name), get())


# definir componente Tabview
tabview = customtkinter.CTkTabview(app, width=950, height=550, fg_color="black")
tabview.place(x=20, y=20)

# Adicionar tabuladores ao tabview
tab1 = tabview.add(" Home ")  # adicionar tab
tab2 = tabview.add(" WebBrowser ")  # adicionar tab 
tab3 = tabview.add(" TKVideoPlayer ")  # adicionar tab
tab4 = tabview.add(" Sound - Mp3 ")  # adicionar tab
tab5 = tabview.add(" Saída ").bind("<Enter>", confirmarSair)  # adicionar tab

# Definir o tabulador ativo / visível num dado momento
tabview.set(" Home ")



"""
TAB 1 - HOME
"""
# FRAME COM IMAGEM INICIAL
image1 = customtkinter.CTkImage(Image.open(".\\images\\others\\home.jpg"), size=(550, 350))

lblImage = customtkinter.CTkLabel(tab1, image = image1, text = "",  width = 550, height = 350)
lblImage.place(x=200, y=50)

lblText = customtkinter.CTkLabel(tab1, text = "Demo - Bibliotecas Media em Python ", font=("Calibri", 24), text_color="cyan")
lblText.place(x=270, y=420)



"""
TAB 2 - WebBrowser
"""
listaCatalogo = TextFiles.lerFicheiroText(fYoutube)  ## carrega ficheiro para lista

# FRAME COM  CATALOGO
frameMenu = customtkinter.CTkScrollableFrame(tab2,  fg_color = "black", width=820, height=440)
frameMenu.place(x=50, y=50)

colID=1
rowID=1
for linha in listaCatalogo:
    if linha.find(";") == -1: continue
    img, title, url = linha.split(";")
    url=url.replace("\n", "")

    image1 = customtkinter.CTkImage(Image.open(f".\\images\\catalog\\{img}"), size=(160, 160))
            
    e = customtkinter.CTkButton(frameMenu, text=title, image = image1, compound="top",  fg_color="ghost white",
                            width = 230, height = 180, font=("Calibri", 14), text_color="black",
                            command= lambda link= url: playWebBrowserVideo(link)).grid(column = colID, row = rowID, padx = 20, pady=20)        
    colID+=1
    if colID == 4:
        rowID+=1
        colID=1
        





"""
TAB 3 - VIDEOPLAYER
"""
listaCatalogo = TextFiles.lerFicheiroText(fVideos)  ## carrega ficheiro para lista


# FRAME COM  CATALOGO
frameMenu3 = customtkinter.CTkScrollableFrame(tab3,  fg_color = "azure2", width=280, height=430)
frameMenu3.place(x=30, y=30)

# FRAME COM  VIDEOPLAY
frameMenu3Play = customtkinter.CTkFrame(tab3,  fg_color = "azure2", width=500, height=440)
frameMenu3Play.place(x=370, y=30)
videoPlayer = TkinterVideo(frameMenu3Play, scaled=True)

videoPlayer.set_size([400,300], True)  # width, height
#videoPlayer.set_scaled=True
videoPlayer.place(x=50, y=10)


# CATALOGO -----------------------------
rowID=1
for linha in listaCatalogo:
    if linha.find(";") == -1: continue
    img, title, mp4File = linha.split(";")
    mp4File=mp4File.replace("\n", "")

    image1 = customtkinter.CTkImage(Image.open(f".\\images\\catalog\\{img}"), size=(128, 128))
            
    e = customtkinter.CTkButton(frameMenu3, text=title, image = image1, compound="top",  fg_color="ghost white",
                            width = 230, height = 180, font=("Calibri", 14), text_color="black",
                            command= lambda mp4FilePlay = mp4File: playSound(mp4FilePlay)).grid(column = 1, row = rowID, padx = 20, pady=20) 
            
    rowID+=2


btnVieoPlay = customtkinter.CTkButton(frameMenu3Play, text= "Play", width=100, height=40, text_color="black", fg_color="azure1", 
                        command = playVideo).place(x=10, y=380)  

btnVideoPause = customtkinter.CTkButton(frameMenu3Play, text= "Pause", width=100, height=40, text_color="black", fg_color="azure1", 
                        command = pauseVideo).place(x=120, y=380)  

btnVideoStop = customtkinter.CTkButton(frameMenu3Play, text= "Stop", width=100, height=40, text_color="black", fg_color="azure1", 
                        command = stopVideo).place(x=240, y=380)  

btnVideoSeek = customtkinter.CTkButton(frameMenu3Play, text= "Seek", width=100, height=40, text_color="black", fg_color="azure1", 
                        command = lambda: seekVideo(30)).place(x=360, y=380)  











"""
TAB 4 - SOUND
"""
listaCatalogo = TextFiles.lerFicheiroText(fSongs)  ## carrega ficheiro para lista

mixer.init() #Initialzing pyamge mixer

# FRAME COM  CATALOGO
frameMenu4 = customtkinter.CTkScrollableFrame(tab4,  fg_color = "azure2", width=820, height=220)
frameMenu4.place(x=50, y=50)

btnPlay = customtkinter.CTkButton(tab4, text= "Play", width=180, height=40, text_color="black", fg_color="azure1", 
                        command = mixerSound).place(x=80, y=450)  

btnPause = customtkinter.CTkButton(tab4, text= "Pause", width=180, height=40, text_color="black", fg_color="azure1", 
                        command = mixerPause).place(x=280, y=450)  

btnStop = customtkinter.CTkButton(tab4, text= "Stop", width=180, height=40, text_color="black", fg_color="azure1", 
                        command = mixerStop).place(x=480, y=450)  

btnVolume = customtkinter.CTkButton(tab4, text= "Volume", width=180, height=40, text_color="black", fg_color="azure1", 
                        command = "").place(x=680, y=450)  

# CATALOGO -----------------------------
colID=1
rowID=1
for linha in listaCatalogo:
    if linha.find(";") == -1: continue
    img, title, mp3File = linha.split(";")
    mp3File=mp3File.replace("\n", "")

    image1 = customtkinter.CTkImage(Image.open(f".\\images\\catalog\\{img}"), size=(128, 128))
            
    e = customtkinter.CTkButton(frameMenu4, text=title, image = image1, compound="top",  fg_color="ghost white",
                            width = 230, height = 180, font=("Calibri", 14), text_color="black",
                            command= lambda link = mp3File: playSound(link)).grid(column = colID, row = rowID, padx = 20, pady=20) 
            
    colID+=1
    if colID == 4:
        rowID+=2
        colID=1













app.mainloop()   # event listening loop by calling the mainloop()
