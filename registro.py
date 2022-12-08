import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Registro de cuenta")
        #setting window size
        width=434
        height=411
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
        GLabel_890["text"] = "Nombre:"
        GLabel_890.place(x=60,y=20,width=70,height=25)

        GLabel_256=tk.Label(root)
        GLabel_256["cursor"] = "trek"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_256["font"] = ft
        GLabel_256["fg"] = "#333333"
        GLabel_256["justify"] = "center"
        GLabel_256["text"] = "Apellido: "
        GLabel_256.place(x=60,y=60,width=70,height=25)

        GLineEdit_540=tk.Entry(root)
        GLineEdit_540["bg"] = "#ffffff"
        GLineEdit_540["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_540["font"] = ft
        GLineEdit_540["fg"] = "#333333"
        GLineEdit_540["justify"] = "center"
        GLineEdit_540["text"] = ""
        GLineEdit_540.place(x=130,y=20,width=250,height=25)

        GLineEdit_411=tk.Entry(root)
        GLineEdit_411["bg"] = "#ffffff"
        GLineEdit_411["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_411["font"] = ft
        GLineEdit_411["fg"] = "#333333"
        GLineEdit_411["justify"] = "center"
        GLineEdit_411["text"] = ""
        GLineEdit_411.place(x=130,y=60,width=250,height=25)

        GButton_305=tk.Button(root)
        GButton_305["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_305["font"] = ft
        GButton_305["fg"] = "#000000"
        GButton_305["justify"] = "center"
        GButton_305["text"] = "Aceptar"
        GButton_305.place(x=260,y=370,width=70,height=25)
        GButton_305["command"] = self.GButton_305_command

        GButton_389=tk.Button(root)
        GButton_389["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_389["font"] = ft
        GButton_389["fg"] = "#000000"
        GButton_389["justify"] = "center"
        GButton_389["text"] = "Cancelar"
        GButton_389.place(x=340,y=370,width=70,height=25)
        GButton_389["command"] = self.GButton_389_command

        GLineEdit_217=tk.Entry(root)
        GLineEdit_217["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_217["font"] = ft
        GLineEdit_217["fg"] = "#333333"
        GLineEdit_217["justify"] = "center"
        GLineEdit_217["text"] = ""
        GLineEdit_217.place(x=130,y=110,width=250,height=25)

        GLabel_318=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_318["font"] = ft
        GLabel_318["fg"] = "#333333"
        GLabel_318["justify"] = "center"
        GLabel_318["text"] = "Correo:"
        GLabel_318.place(x=60,y=110,width=70,height=25)

        GLabel_645=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_645["font"] = ft
        GLabel_645["fg"] = "#333333"
        GLabel_645["justify"] = "center"
        GLabel_645["text"] = "Fecha de nacimiento:"
        GLabel_645.place(x=0,y=150,width=125,height=25)

        GLabel_747=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_747["font"] = ft
        GLabel_747["fg"] = "#333333"
        GLabel_747["justify"] = "center"
        GLabel_747["text"] = "DNI:"
        GLabel_747.place(x=60,y=190,width=70,height=25)

        GLabel_438=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_438["font"] = ft
        GLabel_438["fg"] = "#333333"
        GLabel_438["justify"] = "center"
        GLabel_438["text"] = "Usuario:"
        GLabel_438.place(x=60,y=230,width=70,height=25)

        GLabel_8=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_8["font"] = ft
        GLabel_8["fg"] = "#333333"
        GLabel_8["justify"] = "center"
        GLabel_8["text"] = "Contraseña:"
        GLabel_8.place(x=60,y=270,width=70,height=25)

        GLabel_590=tk.Label(root)
        GLabel_590["anchor"] = "e"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_590["font"] = ft
        GLabel_590["fg"] = "#333333"
        GLabel_590["justify"] = "center"
        GLabel_590["text"] = "Confirmar contraseña:"
        GLabel_590.place(x=0,y=310,width=125,height=30)

        GLineEdit_164=tk.Entry(root)
        GLineEdit_164["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_164["font"] = ft
        GLineEdit_164["fg"] = "#333333"
        GLineEdit_164["justify"] = "center"
        GLineEdit_164["text"] = ""
        GLineEdit_164.place(x=130,y=150,width=150,height=25)

        GLineEdit_869=tk.Entry(root)
        GLineEdit_869["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_869["font"] = ft
        GLineEdit_869["fg"] = "#333333"
        GLineEdit_869["justify"] = "center"
        GLineEdit_869["text"] = ""
        GLineEdit_869.place(x=130,y=190,width=150,height=25)

        GLineEdit_890=tk.Entry(root)
        GLineEdit_890["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_890["font"] = ft
        GLineEdit_890["fg"] = "#333333"
        GLineEdit_890["justify"] = "center"
        GLineEdit_890["text"] = ""
        GLineEdit_890.place(x=130,y=230,width=250,height=25)

        GLineEdit_635=tk.Entry(root)
        GLineEdit_635["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_635["font"] = ft
        GLineEdit_635["fg"] = "#333333"
        GLineEdit_635["justify"] = "center"
        GLineEdit_635["text"] = ""
        GLineEdit_635.place(x=130,y=270,width=250,height=25)

        GLineEdit_230=tk.Entry(root)
        GLineEdit_230["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_230["font"] = ft
        GLineEdit_230["fg"] = "#333333"
        GLineEdit_230["justify"] = "center"
        GLineEdit_230["text"] = ""
        GLineEdit_230.place(x=130,y=320,width=250,height=25)

    def GButton_305_command(self):
        print("command")


    def GButton_389_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
