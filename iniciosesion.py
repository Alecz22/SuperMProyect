import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Inicio de Sesion")
        #setting window size
        width=481
        height=260
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_890=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_890["font"] = ft
        GLabel_890["fg"] = "#333333"
        GLabel_890["justify"] = "center"
        GLabel_890["text"] = "Usuario:"
        GLabel_890.place(x=60,y=50,width=70,height=25)

        GLabel_256=tk.Label(root)
        GLabel_256["cursor"] = "trek"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_256["font"] = ft
        GLabel_256["fg"] = "#333333"
        GLabel_256["justify"] = "center"
        GLabel_256["text"] = "Contraseña: "
        GLabel_256.place(x=60,y=110,width=70,height=25)

        GLineEdit_540=tk.Entry(root)
        GLineEdit_540["bg"] = "#ffffff"
        GLineEdit_540["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_540["font"] = ft
        GLineEdit_540["fg"] = "#333333"
        GLineEdit_540["justify"] = "center"
        GLineEdit_540["text"] = ""
        GLineEdit_540.place(x=140,y=50,width=250,height=30)

        GLineEdit_411=tk.Entry(root)
        GLineEdit_411["bg"] = "#ffffff"
        GLineEdit_411["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_411["font"] = ft
        GLineEdit_411["fg"] = "#333333"
        GLineEdit_411["justify"] = "center"
        GLineEdit_411["text"] = ""
        GLineEdit_411.place(x=140,y=110,width=250,height=30)

        GButton_305=tk.Button(root)
        GButton_305["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_305["font"] = ft
        GButton_305["fg"] = "#000000"
        GButton_305["justify"] = "center"
        GButton_305["text"] = "Aceptar"
        GButton_305.place(x=300,y=210,width=70,height=25)
        GButton_305["command"] = self.GButton_305_command

        GButton_389=tk.Button(root)
        GButton_389["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_389["font"] = ft
        GButton_389["fg"] = "#000000"
        GButton_389["justify"] = "center"
        GButton_389["text"] = "Cancelar"
        GButton_389.place(x=390,y=210,width=70,height=25)
        GButton_389["command"] = self.GButton_389_command

        GMessage_601=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_601["font"] = ft
        GMessage_601["fg"] = "#333333"
        GMessage_601["justify"] = "right"
        GMessage_601["text"] = "¿No posee una cuenta?"
        GMessage_601.place(x=10,y=210,width=200,height=50)

        GButton_559=tk.Button(root)
        GButton_559["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_559["font"] = ft
        GButton_559["fg"] = "#000000"
        GButton_559["justify"] = "center"
        GButton_559["text"] = "Registrarse"
        GButton_559.place(x=190,y=210,width=70,height=25)
        GButton_559["command"] = self.GButton_559_command

    def GButton_305_command(self):
        print("command")


    def GButton_389_command(self):
        print("command")


    def GButton_559_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
