# Biblioteca Tkinter: UI
import customtkinter

# Variavel global com designacao do ficheiro
ficheiro = ".\\files\\texto.txt"


def guarda_ficheiro():
    """
    Guarda conteúdo da Text em ficheiro
    """
    linha = txtTexto.get("0.0","end-1c")    # end - 1 caracter (\n)
    fileText = open(ficheiro, "w", encoding="utf-8")
    fileText.write(linha)
    fileText.close()


# Limpa o conteúdo da Text
def limpar():
    """
    Limpa todo o conteúudo da Text
    """
    txtTexto.delete("0.0", "end")
   


 
def ler_ficheiro():
    """
    Le ficheiro de texto e renderiza na TextBox
    """      
    fileText = open(ficheiro, "r", encoding="utf-8")
    lista = fileText.readlines()   # ler todo o ficheiro para uma lista
    fileText.close()
    limpar() # Limpa o conteúdo que eventualmente esteja na Text, para a seguir adicionar o conteudo do fx
    for linha in lista:
        txtTexto.insert("end", linha)
    

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





# --- GUI DA APLICAÇÃO------------------------------------------------
# invoca classe Tk , cria a "main window"
app = customtkinter.CTk()   # Invoca a classe CTK,
renderWindow(300, 600, "My Notepad")

# Label
labelText = customtkinter.CTkLabel(app, text = "Indique as suas notas", text_color= "blue")
labelText.place(x=90, y=15)

#TextBox 
txtTexto = customtkinter.CTkTextbox(app, width = 250, height = 300)
txtTexto.place(x = 25, y= 50)

# Button Guardar
btnGuardar=customtkinter.CTkButton(app,  text = "Guardar Notas" , width = 250, height = 50,
                  fg_color= "black", text_color="cyan", command = guarda_ficheiro)
btnGuardar.place(x=25, y=360)


# Button Limpar
btnLimpar= customtkinter.CTkButton(app,  text = "Limpar Notas",width = 250, height = 50,   
                fg_color= "black", text_color="cyan", command = limpar)
btnLimpar.place(x=25, y=420)

# Button Ler ficheiro
btnLer= customtkinter.CTkButton(app,  text = "Ler Bloco de Notas", width = 250, height = 50, 
              fg_color= "black", text_color="cyan", command = ler_ficheiro)
btnLer.place(x=25, y=480)


app.mainloop()   # event listening loop by calling the mainloop()