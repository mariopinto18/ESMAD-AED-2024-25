# Biblioteca Tkinter: UI
import customtkinter
from PIL import Image, ImageTk


def calcular_imc():
    """
    calcula IMC com base na altura e do peso
    """
    altura_M = altura.get() /100        # obter altura da Entry e converter e metros
    imc = peso.get() / (altura_M * altura_M)
    str_imc = "{0:.2f}".format(imc)    # Formata com 2 casas decimais
    val_imc.set(str_imc)               # colocar imc na variável associada à label


def sair():
  """
  opção de sair, terminar
  """
  # app.quit()     # fecha o container window
  app.destroy()    # fecha e remove da memoria 


def renderWindow(appWidth, appHeight, appTitle):
    app.title(appTitle)
    # Obter as dimensões do meu screen (em pixeis)
    screenWidth = app.winfo_screenwidth()
    screenHeight = app.winfo_screenheight()
    # App centrada no screen, em função das suas dimensões# encontrar o 
    x = (screenWidth/2) - (appWidth/2)
    y= (screenHeight/2) - (appHeight/2)
    app.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
    app.resizable(False, False) 



# --- GUI DA APLICAÇÃO------------------------------------------------
app = customtkinter.CTk()   # Invoca a classe CTK
renderWindow(325, 670,"Simulador de IMC" )
#customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
#customtkinter.set_appearance_mode("system")  # default
#customtkinter.set_appearance_mode("dark")
#customtkinter.set_appearance_mode("light")

# ----- FRAME INPUT
frameData = customtkinter.CTkFrame(app, width = 300, height = 150, fg_color="gray")
frameData.place(x=10, y=20)

#Label
lblPeso=customtkinter.CTkLabel(frameData, text="Peso   :", 
                              text_color="white", font=("Helvetica", 14))
lblPeso.place(x=25, y=30)

lblAltura=customtkinter.CTkLabel(frameData, text="Altura (cm):", 
                                text_color="white", font=("Helvetica", 14))
lblAltura.place(x=25, y=70)

#Entry
peso = customtkinter.IntVar()
txtPeso=customtkinter.CTkEntry(frameData, width = 85, textvariable=peso)
txtPeso.place(x=120, y=30)

altura = customtkinter.IntVar()
txt_altura=customtkinter.CTkEntry(frameData, width = 85, textvariable=altura)
txt_altura.place(x=120, y=70)


#BUTTONS
btnIMC=customtkinter.CTkButton(app,  text = "Calcular \nIMC" , width = 300, height = 60,
                                command = calcular_imc)
btnIMC.place(x=10, y=190)

btn_PesoIdeal=customtkinter.CTkButton(app,  text = "Sair" , width = 300, height = 60,  
                              command=sair)
btn_PesoIdeal.place(x=10, y=265)


# FRAME OUTPUT
frameIMC = customtkinter.CTkFrame(app, width = 300, height = 100, fg_color="gray")
frameIMC.place(x=10, y=340)

lblImcText = customtkinter.CTkLabel(frameIMC, text = "Índice de Massa Corporal", font = ("Helvetica", 16), 
                                    text_color= "cyan")
lblImcText.place(x=40, y=10)

val_imc = customtkinter.StringVar()           # variavel associada à label que mostra o resultado
lblImc = customtkinter.CTkLabel(frameIMC, textvariable = val_imc, font = ("Helvetica",  18),
                        text_color="cyan")
lblImc.place(x=110, y=55)

# IMAGEM EM BUTTON
"""
imgButton = customtkinter.CTkImage(Image.open(".\\images\\imc.gif"), size=(280, 160))

btnIMC=customtkinter.CTkButton(app, image= imgButton , width = 280, height = 160,
                      fg_color="transparent")
btnIMC.place(x=10, y=470)
"""
#frameIMC.place_forget()
#frameIMC.place(x=10, y=340)


# ------- Imagem EM LABEL
imgButton = customtkinter.CTkImage(Image.open(".\\images\\imc.gif"), size=(280, 160))

btnIMC=customtkinter.CTkLabel(app, image= imgButton , width = 280, height = 160,
                      fg_color="transparent")
btnIMC.place(x=10, y=470)



app.mainloop()   # event listening loop by calling the mainloop()