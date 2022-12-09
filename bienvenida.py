import tkinter as tk
import tkinter.font as tkFont
from  dal.db import Db
from iniciosesion import Inicio

class App:
    def __init__(self, root, title):
        self.root=root
        root.title(title)
        width=446
        height=130
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_325=tk.Button(root)
        GButton_325["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_325["font"] = ft
        GButton_325["fg"] = "#000000"
        GButton_325["justify"] = "center"
        GButton_325["text"] = "Entrar al Super"
        GButton_325.place(x=100,y=60,width=250,height=35)
        GButton_325["command"] = self.abrir_iniciosesion

        GMessage_423=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_423["font"] = ft
        GMessage_423["fg"] = "#333333"
        GMessage_423["justify"] = "center"
        GMessage_423["text"] = "¡Bienvenido a Supermarket!"
        GMessage_423.place(x=70,y=5,width=303,height=50)

    def abrir_iniciosesion(self):
        Inicio(self.root)

if __name__ == "__main__":
    Db.crear_tablas()
    Db.poblar_tablas()
    project= "supermarket"
    root = tk.Tk()
    root.iconbitmap(default=f"{project}.ico")
    app = App(root, project.capitalize())
    root.mainloop()
