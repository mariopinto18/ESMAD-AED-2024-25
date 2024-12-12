# Biblioteca CustomTkinter
import customtkinter
from PIL import Image, ImageTk



def CalcPesoIdeal():
    """
    Determina o peso ideal em função do genero e altura
    """
    alturaValue = int(altura.get())
    k=4
    if genero.get() == "Masculino":
        k=4
    else:
        k=2
    # Obter valor da Entry altura: altura.get()
    peso = (alturaValue - 100) - (alturaValue - 150)/k
    pesoIdeal.set(str(peso))
    



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
renderWindow(370, 430, "Simulador Peso Ideal")

#Label
lblAltura=customtkinter.CTkLabel(app, text="Altura em cm:", text_color="blue", font=("Helvetica", 14))
lblAltura.place(x=50, y=30)

#Entry ALtura
altura = customtkinter.StringVar()
txtAltura=customtkinter.CTkEntry(app, width = 150, textvariable = altura, 
                                placeholder_text= "Altura em cm")
txtAltura.place(x=170, y=30)


# Label 
lblGenero=customtkinter.CTkLabel(app, text="Género:", text_color="blue", font=("Helvetica", 14) )
lblGenero.place(x=50, y=70)

#Radiobutton
genero = customtkinter.StringVar()
genero.set("Masculino")   # Opção selecionada por defeito
rd1 = customtkinter.CTkRadioButton(app, text = "Masculino", value = "Masculino", variable = genero)
rd1.place(x=170, y=90)
rd2 = customtkinter.CTkRadioButton(app, text = "Feminino", value = "Feminino", variable =  genero)
rd2.place(x=170, y=130)


#Button
imgBtnPesoIdeal = customtkinter.CTkImage(Image.open(".\\images\\PesoIdeal.png"), size=(64, 64))

btnPesoIdeal=customtkinter.CTkButton(app,  text = "Calcular Peso Ideal" , width = 330, height = 80, 
                            fg_color= "black", text_color="cyan",  image = imgBtnPesoIdeal, 
                            compound="right", command = CalcPesoIdeal)
btnPesoIdeal.place(x=20, y=180)

# Label Peso Ideal
lblPesoIdeal=customtkinter.CTkLabel(app, text="Peso Ideal em Kg",  text_color="red", font=("Helvetica", 17))
lblPesoIdeal.place(x=100, y=300)


#Entry
pesoIdeal=customtkinter.StringVar()
txtPesoIdeal=customtkinter.CTkEntry(app, width = 70, state = "disabled" , font= ("Helvetica bold", 17),
                         fg_color="transparent", text_color="blue" , border_width=0, textvariable = pesoIdeal)
txtPesoIdeal.place(x=145, y=335)

app.mainloop()   # event listening loop by calling the mainloop()